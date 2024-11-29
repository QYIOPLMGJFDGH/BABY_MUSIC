import asyncio
from datetime import datetime, timedelta
from pymongo import MongoClient
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait
from SONALI import app
from config import OWNER_ID
from SONALI.utils.database import (
    get_active_chats,
    get_authuser_names,
    get_client,
    get_served_chats,
    get_served_users,
)
from SONALI.utils.decorators.language import language
from SONALI.utils.formatters import alpha_to_int
from config import adminlist

# MongoDB सेटअप
client = MongoClient("mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority")  # MongoDB URI
db = client["subscriberDB"]
subscribers = db["subscribers"]

IS_BROADCASTING = False


# Subscriber को जोड़ने का फंक्शन
async def add_subscriber(user_id, days):
    expiry_date = datetime.now() + timedelta(days=days)
    subscribers.update_one(
        {"user_id": user_id},
        {"$set": {"expiry_date": expiry_date, "usage_count": 0}},
        upsert=True,
    )
    return True


# Subscriber को हटाने का फंक्शन
async def remove_subscriber(user_id):
    subscribers.delete_one({"user_id": user_id})
    return True


# Expired subscribers को हटाने का बैकग्राउंड टास्क
async def clean_expired_subscribers():
    while True:
        now = datetime.now()
        subscribers.delete_many({"expiry_date": {"$lt": now}})
        await asyncio.sleep(3600)  # हर घंटे चेक करें


# Add Subscriber Command
@app.on_message(filters.command("add"))
async def add_command(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("यह कमांड केवल Owner उपयोग कर सकते हैं।")

    try:
        args = message.text.split()
        user_id = int(args[1])
        days = int(args[2])
        await add_subscriber(user_id, days)
        await message.reply(f"User {user_id} को {days} दिन के लिए सब्सक्राइबर लिस्ट में जोड़ा गया।")
    except:
        await message.reply("कृपया सही फॉर्मेट में कमांड डालें: `/add user_id days`")


# Remove Subscriber Command
@app.on_message(filters.command("rm"))
async def remove_command(client, message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("यह कमांड केवल Owner उपयोग कर सकते हैं।")

    try:
        args = message.text.split()
        user_id = int(args[1])
        await remove_subscriber(user_id)
        await message.reply(f"User {user_id} को सब्सक्राइबर लिस्ट से हटा दिया गया।")
    except:
        await message.reply("कृपया सही फॉर्मेट में कमांड डालें: `/rm user_id`")


# Broadcast Command
@app.on_message(filters.command("broadcast"))
@language
async def broadcast_message(client, message, _):
    global IS_BROADCASTING
    user_id = message.from_user.id

    # Owner चेक
    if user_id != OWNER_ID:
        user = subscribers.find_one({"user_id": user_id})
        if not user:
            return await message.reply("आप सब्सक्राइबर लिस्ट में नहीं हैं।")

        # Usage limit चेक करें
        if user["usage_count"] >= 3:
            return await message.reply("आपने आज की लिमिट पूरी कर ली है। कृपया 24 घंटे बाद कोशिश करें।")

        # Usage count बढ़ाएं
        subscribers.update_one({"user_id": user_id}, {"$inc": {"usage_count": 1}})

    # Broadcast Logic
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1]
        query = query.replace("-pin", "").replace("-nobot", "").replace("-pinloud", "").replace("-assistant", "").replace("-user", "")
        if query == "":
            return await message.reply_text(_["broad_8"])

    IS_BROADCASTING = True
    await message.reply_text(_["broad_1"])

    # ब्रॉडकास्ट संदेश भेजना
    sent = 0
    pin = 0
    schats = await get_served_chats()
    chats = [int(chat["chat_id"]) for chat in schats]
    for i in chats:
        try:
            m = await app.forward_messages(i, y, x) if message.reply_to_message else await app.send_message(i, text=query)
            if "-pin" in message.text:
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except:
                    continue
            elif "-pinloud" in message.text:
                try:
                    await m.pin(disable_notification=False)
                    pin += 1
                except:
                    continue
            sent += 1
            await asyncio.sleep(0.2)
        except FloodWait as fw:
            await asyncio.sleep(fw.value)
        except:
            continue

    try:
        await message.reply_text(_["broad_3"].format(sent, pin))
    except:
        pass

    IS_BROADCASTING = False


# Auto-clean Task
async def auto_clean():
    while not await asyncio.sleep(10):
        try:
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    async for user in app.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS):
                        if user.privileges.can_manage_video_chats:
                            adminlist[chat_id].append(user.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for user in authusers:
                        user_id = await alpha_to_int(user)
                        adminlist[chat_id].append(user_id)
        except:
            continue


# Background Tasks
asyncio.create_task(auto_clean())
asyncio.create_task(clean_expired_subscribers())
        
