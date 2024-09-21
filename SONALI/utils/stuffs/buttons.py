from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    BBUTTON = [[InlineKeyboardButton("• ɢꝛᴏᴜᴘ •", callback_data="mplus HELP_Group"),InlineKeyboardButton("• ᴧᴄᴛɪᴏи •", callback_data="mplus HELP_Action"),InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("• ᴛᴧɢ-ᴧʟʟ •", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("• ɪᴍᴘᴏsᴛᴇꝛ •", callback_data="mplus HELP_Imposter"),InlineKeyboardButton("• ᴛ-ᴅᴧꝛᴇ •", callback_data="mplus HELP_TD")],
    [InlineKeyboardButton("• ʜᴧsʜ-ᴛᴧɢ •", callback_data="mplus HELP_HT")],
    [InlineKeyboardButton("• ттѕ •", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("• ғᴜи •", callback_data="mplus HELP_Fun")],    
    [InlineKeyboardButton("↺ ʙᴀᴄᴋ ↻", callback_data=f"settings_back_helper"), 
    ]]
    
    MBUTTON = [[InlineKeyboardButton("• ᴀɪ •", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("• ɪɴғᴏ •", callback_data="mplus HELP_Info"),InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("• ᴇxᴛꝛᴧ •", callback_data="mplus HELP_Extra"),
    InlineKeyboardButton("• ɪᴍᴧɢᴇ •", callback_data="mplus HELP_Image"),InlineKeyboardButton("• sᴇᴧꝛᴄʜ •", callback_data="mplus HELP_Search")],
    [InlineKeyboardButton("• ǫᴜɪʟʏ •", callback_data="mplus HELP_Q")],
    [InlineKeyboardButton("• ғᴏиᴛ •", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("• ɢᴧᴍᴇ •", callback_data="mplus HELP_Game"),InlineKeyboardButton("• ᴛ-ɢꝛᴧᴘʜ •", callback_data="mplus HELP_TG")],    
    [InlineKeyboardButton("↺ ʙᴀᴄᴋ ↻", callback_data=f"settings_back_helper"), 
    ]]

    UBUTTON = [[InlineKeyboardButton("• ᴍᴜsɪᴄ •", callback_data="settings_back_helper"),InlineKeyboardButton("• ᴛᴏᴏʟs •", callback_data=f"mbot_cb")],[InlineKeyboardButton("• ᴍᴀɴᴀɢᴇ •", callback_data=f"bbot_cb"),
    InlineKeyboardButton("• ʀᴀɪᴅ •", callback_data="mplus HELP_raid")],[InlineKeyboardButton("↺ ʙᴀᴄᴋ ↻", callback_data=f"settingsback_helper"),
    ]]
