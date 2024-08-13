from pyrogram.types import InlineKeyboardButton

import config
from YousefMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="S_B_1",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text=" 𝑫𝒆𝒗 ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="S_B_1",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text=" 𝑫𝒆𝒗 ", user_id=config.OWNER_ID),
            InlineKeyboardButton(text=config.CHANNEL_NAME, url=config.CHANNEL_LINK),
        ],
    ]
    return buttons
