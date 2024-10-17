import asyncio
import os
from datetime import datetime, timedelta
from typing import Union

from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded

import config
from SONALI import LOGGER, YouTube, app
from SONALI.misc import db
from SONALI.utils.database import (
    add_active_chat, add_active_video_chat, get_lang, get_loop, group_assistant, is_autoend,
    music_on, remove_active_chat, remove_active_video_chat, set_loop
)
from SONALI.utils.exceptions import AssistantErr
from SONALI.utils.formatters import check_duration, seconds_to_min, speed_converter
from SONALI.utils.inline.play import stream_markup, telegram_markup
from SONALI.utils.stream.autoclear import auto_clean
from SONALI.utils.thumbnails import get_thumb
from strings import get_string

autoend, counter = {}, {}

async def _clear_(chat_id):
    db[chat_id] = []
    await remove_active_video_chat(chat_id)
    await remove_active_chat(chat_id)

class Call(PyTgCalls):
    def __init__(self):
        self.clients = [
            self._create_client(i) for i in range(1, 6) if getattr(config, f"STRING{i}")
        ]
    
    def _create_client(self, i):
        userbot = Client(
            name=f"RAUSHANAss{i}", 
            api_id=config.API_ID, 
            api_hash=config.API_HASH, 
            session_string=str(getattr(config, f"STRING{i}"))
        )
        return PyTgCalls(userbot, cache_duration=100)

    async def _manage_stream(self, chat_id, method, *args):
        assistant = await group_assistant(self, chat_id)
        await getattr(assistant, method)(chat_id, *args)

    async def pause_stream(self, chat_id): await self._manage_stream(chat_id, 'pause_stream')
    async def resume_stream(self, chat_id): await self._manage_stream(chat_id, 'resume_stream')
    async def stop_stream(self, chat_id): await self._manage_stream(chat_id, 'leave_group_call')

    async def stop_stream_force(self, chat_id):
        for client in self.clients:
            try: await client.leave_group_call(chat_id)
            except: pass
        await _clear_(chat_id)

    async def speedup_stream(self, chat_id, file_path, speed, playing):
        assistant = await group_assistant(self, chat_id)
        if str(speed) != "1.0":
            out = await self._process_speed(file_path, speed)
        else:
            out = file_path
        await self._change_stream(chat_id, assistant, out, playing)

    async def _process_speed(self, file_path, speed):
        chatdir = os.path.join(os.getcwd(), "playback", str(speed))
        if not os.path.isdir(chatdir):
            os.makedirs(chatdir)
        out = os.path.join(chatdir, os.path.basename(file_path))
        if not os.path.isfile(out):
            vs = {"0.5": 2.0, "0.75": 1.35, "1.5": 0.68, "2.0": 0.5}.get(str(speed), 1.0)
            cmd = f"ffmpeg -i {file_path} -filter:v setpts={vs}*PTS -filter:a atempo={speed} {out}"
            proc = await asyncio.create_subprocess_shell(cmd)
            await proc.communicate()
        return out

    async def _change_stream(self, chat_id, assistant, file_path, playing):
        dur = await asyncio.get_event_loop().run_in_executor(None, check_duration, file_path)
        played, con_seconds = speed_converter(playing[0]["played"], speed)
        stream = AudioVideoPiped(file_path, audio_parameters=HighQualityAudio()) \
            if playing[0]["streamtype"] == "video" else AudioPiped(file_path, audio_parameters=HighQualityAudio())
        await assistant.change_stream(chat_id, stream)
        db[chat_id][0].update({"played": con_seconds, "dur": seconds_to_min(dur), "seconds": dur, "speed_path": file_path, "speed": speed})

    async def change_stream(self, client, chat_id):
        check, loop = db.get(chat_id), await get_loop(chat_id)
        try:
            if loop == 0:
                check.pop(0)
            else:
                await set_loop(chat_id, loop - 1)
            await auto_clean(check[0])
        except:
            await _clear_(chat_id)
            return await client.leave_group_call(chat_id)
        
        await self._play_next(client, chat_id, check)

    async def _play_next(self, client, chat_id, check):
        queued, streamtype = check[0]["file"], check[0]["streamtype"]
        video = streamtype == "video"
        stream = AudioVideoPiped(queued, audio_parameters=HighQualityAudio()) if video else AudioPiped(queued)
        await client.change_stream(chat_id, stream)

    async def ping(self):
        pings = [await client.ping for client in self.clients]
        return str(round(sum(pings) / len(pings), 3))

    async def start(self):
        LOGGER(__name__).info("Starting PyTgCalls Client...\n")
        await asyncio.gather(*[client.start() for client in self.clients])

    async def decorators(self):
        @self.clients[0].on_kicked()
        async def stream_services_handler(_, chat_id): await self.stop_stream(chat_id)

        @self.clients[0].on_stream_end()
        async def stream_end_handler1(client, update): 
            if isinstance(update, StreamAudioEnded):
                await self.change_stream(client, update.chat_id)

RAUSHAN = Call()
