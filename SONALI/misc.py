import time

import heroku3
from pyrogram import filters

import config
from SONALI.core.mongo import mongodb

# logging.py
import logging

def LOGGER(name):
    logging.basicConfig(level=logging.INFO)
    return logging.getLogger(name)

SUDOERS = filters.user()

HAPP = None
_boot_ = time.time()


XCB = [
    "/",
    "@",
    ".",
    "com",
    ":",
    "git",
    "heroku",
    "push",
    str(config.HEROKU_API_KEY),
    "https",
    str(config.HEROKU_APP_NAME),
    "HEAD",
    "master",
]


def dbb():
    global db
    db = {}
    LOGGER(__name__).info(f"❍ Dᴀᴛᴀ ʙᴀsᴇ ʟᴏᴀᴅᴇᴅ......")


async def sudo():
    global SUDOERS
    SUDOERS.add(config.OWNER_ID)
    sudoersdb = mongodb.sudoers
    sudoers = await sudoersdb.find_one({"sudo": "sudo"})
    sudoers = [] if not sudoers else sudoers["sudoers"]
    if config.OWNER_ID not in sudoers:
        sudoers.append(config.OWNER_ID)
        await sudoersdb.update_one(
            {"sudo": "sudo"},
            {"$set": {"sudoers": sudoers}},
            upsert=True,
        )
    if sudoers:
        for user_id in sudoers:
            SUDOERS.add(user_id)
    LOGGER(__name__).info(f"❍ Sᴜᴅᴏ ᴜsᴇʀ ᴠᴇʀɪғɪᴇᴅ.")


def heroku():
    global HAPP
    if heroku:
        if config.HEROKU_API_KEY and config.HEROKU_APP_NAME:
            try:
                Heroku = heroku3.from_key(config.HEROKU_API_KEY)
                HAPP = Heroku.app(config.HEROKU_APP_NAME)
                LOGGER(__name__).info(f"❍ Hᴇʀᴜᴋᴏ ᴀᴘᴘ ɴᴀᴍᴇ ʟᴏᴀᴅ..")
            except BaseException:
                LOGGER(__name__).warning(
                    f"❍ Yᴏᴜ ʜᴀᴠᴇ ɴᴏᴛ ғɪʟʟᴇᴅ ʜᴇʀᴜᴋᴏ ᴀᴘɪ ᴋᴇʏ ᴀɴᴅ ʜᴇʀᴜᴋᴏ ᴀᴘᴘ ɴᴀᴍᴇ ᴄᴏʀʀᴇᴄᴛ...."
                )
