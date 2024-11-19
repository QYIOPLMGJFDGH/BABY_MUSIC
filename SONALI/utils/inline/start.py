from pyrogram.types import InlineKeyboardButton

import config
from SONALI import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_12"], callback_data=f"modebot_cb"),
        ],
        [
            InlineKeyboardButton(text=_["S_B_6"], callback_data=f"abot_cb"),
            InlineKeyboardButton(text=_["S_B_99"], url="https://github.com/BABY-MUSIC/SPOTIFY_MUSIC"),
        ],
    ]
    return buttons
