from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from SONALI import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text="• ʙᴀᴄᴋ •",
            callback_data=f"settingsback_helper",
        ),
       
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• ᴧᴅᴍɪɴ •",
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text="• ᴧᴜᴛʜ •",
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text="• ɢ-ᴄᴧsᴛ •",
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ʙʟ-ᴄʜᴧᴛ •",
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text="• ʙʟ-ᴜsᴇʀs •",
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text="• ᴄ-ᴘʟᴧʏ •",
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ɢ-ʙᴧɴ •",
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text="• ʟᴏᴏᴘ •",
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text="• ʟᴏɢ •",
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• ᴘɪɴɢ •",
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text="• ᴘʟᴀʏ •",
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text="• sʜᴜғғɪʟᴇ •",
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="• sᴇᴇᴋ •",
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text="• sᴏɴɢ •",
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text="• sᴘᴇᴇᴅ •",
                    callback_data="help_callback hb15",
                ),
            ], 
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="• ʙᴀᴄᴋ •",
                    callback_data=f"settings_back_helper",
                ),
                InlineKeyboardButton(text="• ᴄʟᴏsᴇ •", callback_data=f"close"),
            ],
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="• ᴏᴘᴇɴ ɪɴ ᴘʀɪᴠɪᴛᴇ •", url=f"https://t.me/{app.username}?start=help"
            ),
        ],
    ]
    return buttons
