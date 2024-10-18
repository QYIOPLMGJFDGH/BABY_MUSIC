from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="˹ ᴘɾꪮɱꪮᴛιꪮɳ ᴀʋᴀιʅᴀʙʅҽ ˼", callback_data=f"promotext"),
        ],
        [
            InlineKeyboardButton(text="˹ ⚘ sƙιᴘ ᴀɳᴅ ❣ ᴘʅᴀʏ ɳꪮɯ ⚘ ˼", callback_data=f"ADMIN Skip|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="˹ ᴜᴘᴅᴀᴛҽ ˼", url="https://t.me/BABY09_WORLD",
            ),
            InlineKeyboardButton(
                text="• 𝛅ᴜᴘᴘᴏꝛᴛ •", url="https://t.me/+OL6jdTL7JAJjYzVl",
            )
        ],
        [
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="𝛓ʟᴏsᴇ"),
        ]
    ]
    return buttons
