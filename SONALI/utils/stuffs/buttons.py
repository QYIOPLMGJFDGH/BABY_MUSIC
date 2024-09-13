from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    BBUTTON = [[InlineKeyboardButton("• ɢꝛᴏᴜᴘ •", callback_data="mplus HELP_Group"),InlineKeyboardButton("• ᴧᴄᴛɪᴏи •", callback_data="mplus HELP_Action"),InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("• ᴛᴧɢ-ᴧʟʟ •", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("• ɪᴍᴘᴏsᴛᴇꝛ •", callback_data="mplus HELP_Imposter"),InlineKeyboardButton("• ᴛ-ᴅᴧꝛᴇ •", callback_data="mplus HELP_TD")],
    [InlineKeyboardButton("• ʜᴧsʜ-ᴛᴧɢ •", callback_data="mplus HELP_HT")],
    [InlineKeyboardButton("• ттѕ •", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("• ғᴜи •", callback_data="mplus HELP_Fun")],    
    [InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data=f"settingsback_helper"), 
    ]]
