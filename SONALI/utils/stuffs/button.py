from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton1, Message
from pyrogram import Client, filters, enums 
class BUTTON(object):
    MBUTTON = [[InlineKeyboardButton1("• ᴀɪ •", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton1("• ɪɴғᴏ •", callback_data="mplus HELP_Info"),InlineKeyboardButton("• sᴛɪᴄᴋᴇꝛ •", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton1("• ᴇxᴛꝛᴧ •", callback_data="mplus HELP_Extra"),
    InlineKeyboardButton1("• ɪᴍᴧɢᴇ •", callback_data="mplus HELP_Image"),InlineKeyboardButton1("• sᴇᴧꝛᴄʜ •", callback_data="mplus HELP_Search")],
    [InlineKeyboardButton1("• ǫᴜɪʟʏ •", callback_data="mplus HELP_Q")],
    [InlineKeyboardButton1("• ғᴏиᴛ •", callback_data="mplus HELP_Font"),
    InlineKeyboardButton1("• ɢᴧᴍᴇ •", callback_data="mplus HELP_Game"),InlineKeyboardButton1("• ᴛ-ɢꝛᴧᴘʜ •", callback_data="mplus HELP_TG")],    
    [InlineKeyboardButton1("• ʙᴀᴄᴋ •", callback_data=f"settingsback_helper"), 
    ]]
