from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    BBUTTON = [[InlineKeyboardButton("• ɢꝛᴏᴜᴘ •", callback_data="dplus HELP_Group"),InlineKeyboardButton("• ᴧᴄᴛɪᴏи •", callback_data="dplus HELP_Action"),InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="dplus HELP_Sticker")],
    [InlineKeyboardButton("• ᴛᴧɢ-ᴧʟʟ •", callback_data="dplus HELP_TagAll"),
    InlineKeyboardButton("• ɪᴍᴘᴏsᴛᴇꝛ •", callback_data="dplus HELP_Imposter"),InlineKeyboardButton("• ᴛ-ᴅᴧꝛᴇ •", callback_data="dplus HELP_TD")],
    [InlineKeyboardButton("• ʜᴧsʜ-ᴛᴧɢ •", callback_data="dplus HELP_HT")],
    [InlineKeyboardButton("• ттѕ •", callback_data="dplus HELP_TTS"),
    InlineKeyboardButton("• ғᴜи •", callback_data="dplus HELP_Fun")],    
    [InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"modebot_cb"), 
    ]]
    
    MBUTTON = [[InlineKeyboardButton("• ᴀɪ •", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("• ɪɴғᴏ •", callback_data="mplus HELP_Info"),InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("• ᴇxᴛꝛᴧ •", callback_data="mplus HELP_Extra"),
    InlineKeyboardButton("• ɪᴍᴧɢᴇ •", callback_data="mplus HELP_Image"),InlineKeyboardButton("• sᴇᴧꝛᴄʜ •", callback_data="mplus HELP_Search")],
    [InlineKeyboardButton("• ǫᴜɪʟʏ •", callback_data="mplus HELP_Q")],
    [InlineKeyboardButton("• ғᴏиᴛ •", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("• ɢᴧᴍᴇ •", callback_data="mplus HELP_Game"),InlineKeyboardButton("• ᴛ-ɢꝛᴧᴘʜ •", callback_data="mplus HELP_TG")],    
    [InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"modebot_cb"), 
    ]]

    ABUTTON = [[InlineKeyboardButton("˹ sᴜᴘᴘᴏꝛᴛ ˼", url="https://t.me/+OL6jdTL7JAJjYzVl")],[InlineKeyboardButton("˹ ᴜᴘᴅᴧᴛᴇ ˼", url="https://t.me/BABY09_WORLD"),
    InlineKeyboardButton("˹ ᴧʟʟ ʙᴏᴛ ˼", url="https://t.me/+tHAENx_r_mtlODZl")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"settingsback_helper"),
    ]]

    UBUTTON = [[InlineKeyboardButton("˹ ᴍᴜsɪᴄ ˼", callback_data="settings_back_helper"),InlineKeyboardButton("˹ ᴛᴏᴏʟs ˼", callback_data=f"mbot_cb")],[InlineKeyboardButton("˹ ᴍᴧɴᴧɢᴇ ˼", callback_data=f"bbot_cb"),
    InlineKeyboardButton("˹ ʀᴧɪᴅ ˼", callback_data="cplus HELP_raid")],[InlineKeyboardButton("↺ ʙᴧᴄᴋ ↻", callback_data=f"settingsback_helper"),
    ]]

