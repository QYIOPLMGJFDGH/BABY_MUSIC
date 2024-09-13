from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("• ᴀɪ •", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("• ɪɴғᴏ •", callback_data="mplus HELP_Info"),InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("• ᴇxᴛꝛᴧ •", callback_data="mplus HELP_Extra"),
    InlineKeyboardButton("• ɪᴍᴧɢᴇ •", callback_data="mplus HELP_Image"),InlineKeyboardButton("• sᴇᴧꝛᴄʜ •", callback_data="mplus HELP_Search")],
    [InlineKeyboardButton("• ǫᴜɪʟʏ •", callback_data="mplus HELP_Q")],
    [InlineKeyboardButton("• ғᴏиᴛ •", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("• ɢᴧᴍᴇ •", callback_data="mplus HELP_Game"),InlineKeyboardButton("• ᴛ-ɢꝛᴧᴘʜ •", callback_data="mplus HELP_TG")],    
    [InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data=f"settingsback_helper"), 
    ]]
