from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated, Message
from pyrogram.errors import UserAlreadyParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from logging import getLogger
from SONALI import app

LOGGER = getLogger(__name__)

# Simplified database for welcome settings
class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        if chat_id not in self.data:
            self.data[chat_id] = {"state": "on"}  # Default state is "on"

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message: Message):
    usage = "**ᴜsᴀɢᴇ:**\n**❍ /welcome [on|off]**"
    if len(message.command) == 1:
        return await message.reply_text(usage)

    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()

        if state == "off":
            if A:
                await message.reply_text("**❍ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ !**")
            else:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"**❍ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴅɪsᴀʙʟᴇᴅ ɪɴ** {message.chat.title}")
        elif state == "on":
            if not A:
                await message.reply_text("**❍ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ.**")
            else:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"**❍ ᴇɴᴀʙʟᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɪɴ** {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("**❍ sᴏʀʀʏ ᴏɴʟʏ ᴀᴅᴍɪɴs ᴄᴀɴ ᴇɴᴀʙʟᴇ ᴡᴇʟᴄᴏᴍᴇ ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ!**")


@app.on_chat_member_updated(filters.group)
async def greet_new_member(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    user = member.new_chat_member.user if member.new_chat_member else member.from_user

    # Check if the welcome messages are enabled
    A = await wlcm.find_one(chat_id)

    # If the user has just joined the group and is not kicked
    if member.new_chat_member and not member.old_chat_member and member.new_chat_member.status != "kicked":

        # Only proceed if welcome messages are enabled
        if A:
            try:
                # Send a simple welcome message
                await app.send_message(
                    chat_id,
                    f"Hello {user.mention}, welcome to {member.chat.title}!"
                )
            except Exception as e:
                LOGGER.error(f"Error while sending welcome message: {e}")
