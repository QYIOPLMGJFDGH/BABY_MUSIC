import asyncio
from datetime import datetime

from pyrogram.enums import ChatType

import config
from SONALI import app
from SONALI.core.call import RAUSHAN, autoend
from SONALI.utils.database import get_client, is_active_chat, is_autoend


# ऑटो लीव फंक्शन
async def auto_leave():
    if config.AUTO_LEAVING_ASSISTANT:
        while not await asyncio.sleep(900):  # हर 15 मिनट में चेक करता रहेगा
            from SONALI.core.userbot import assistants

            for num in assistants:
                client = await get_client(num)
                left = 0
                try:
                    async for i in client.get_dialogs():
                        if i.chat.type in [
                            ChatType.SUPERGROUP,
                            ChatType.GROUP,
                            ChatType.CHANNEL,
                        ]:
                            if (
                                i.chat.id != config.LOGGER_ID
                                and i.chat.id != -1001465277194
                                and i.chat.id != -1002120144597
                            ):
                                if left == 20:
                                    continue
                                if not await is_active_chat(i.chat.id):
                                    try:
                                        await client.leave_chat(i.chat.id)
                                        left += 1
                                    except:
                                        continue
                except:
                    pass


# ऑटो एंड फंक्शन
async def auto_end():
    while not await asyncio.sleep(5):  # हर 5 सेकंड में चेक करता है
        ender = await is_autoend()
        if not ender:
            continue
        for chat_id in autoend:
            timer = autoend.get(chat_id)
            if not timer:
                continue
            if datetime.now() > timer:
                if not await is_active_chat(chat_id):
                    autoend[chat_id] = {}
                    continue

                autoend[chat_id] = {}
                try:
                    # वॉयस चैट के पार्टिसिपेंट्स चेक करें
                    userbot = await get_client(chat_id)
                    call_participants = await userbot.get_call_members(chat_id)

                    if len(call_participants) <= 1:  # अगर सिर्फ बॉट है
                        await app.send_message(
                            chat_id,
                            "❍ ɴᴏ ᴏɴᴇ ɪs ʟɪsᴛᴇɴɪɴɢ ᴛᴏ sᴏɴɢ ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.\n"
                            "ᴘʟᴇᴀsᴇ ᴊᴏɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴏᴛʜᴇʀᴡɪsᴇ ʙᴏᴛ ᴡɪʟʟ ᴇɴᴅ sᴏɴɢ ɪɴ 15 sᴇᴄᴏɴᴅs.",
                        )

                        await asyncio.sleep(15)  # 15 सेकंड का इंतजार करें

                        # फिर से चेक करें कि कोई अन्य सदस्य जुड़ा है या नहीं
                        call_participants = await userbot.get_call_members(chat_id)

                        if len(call_participants) <= 1:  # अगर कोई अन्य सदस्य नहीं है
                            await RAUSHAN.stop_stream(chat_id)
                            await app.send_message(
                                chat_id,
                                "❍ ɴᴏ ᴏɴᴇ ᴊᴏɪɴᴇᴅ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ, sᴏ ᴛʜᴇ sᴏɴɢ ɪs ᴇɴᴅɪɴɢ ᴅᴜᴇ ᴛᴏ ɪɴᴀᴄᴛɪᴠɪᴛʏ.",
                            )
                            continue

                except Exception as e:
                    print(f"Error: {e}")
                    pass

                try:
                    await RAUSHAN.stop_stream(chat_id)
                except:
                    pass
                try:
                    await app.send_message(
                        chat_id,
                        "𝐎ʜʜ 𝐍ᴏ 𝐒ᴏɴɢ 𝐄ɴᴅ 𝐊ᴏɪ 𝐍ᴀ 𝐌ᴀɪ 𝐉ᴀ 𝐑ᴀʜɪ 𝐇ᴜ😐 𝐀ᴀᴛɪ 𝐇ᴜ 𝐅ɪʀ🤭",
                    )
                except:
                    pass


# दोनों फंक्शन्स को असिंक्रोनस रूप से शुरू करें
asyncio.create_task(auto_leave())
asyncio.create_task(auto_end())
