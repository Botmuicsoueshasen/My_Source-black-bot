import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YousefMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YousefMusic import app
from random import  choice, randint
@app.on_message(
    command(["صورص","سورس","السورس","• السورس •", "سبارك"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/2577f47589c4b4c63e4a6.jpg",
        caption=f"""
  - 𓏺[𝙎𝙊𝙐𝙍𝘾𝙀 . 𝖠 ' 𝟣𝟣𝟣 .](https://t.me/cecrr) 
—————————————
-   [𝙗𝙤𝙩 𝙘𝙝𝙖𝙩 𝗕𝗹𝗮𝗰𝗸 .](https://t.me/F6Z_bot) 

-  [𝙨𝙤𝙪𝙧𝙘𝙚 𝙙𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧](https://t.me/y_o_v) 
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⛥ 𓏺 َ𝗬𝗼𝘂𝘀𝗲𝗳 .", url=f"https://t.me/cecrr"), 
                ],[
                    InlineKeyboardButton(
                        ". 𝖠 ' 𝟣𝟣𝟣 .", url=f"t.me/cecrr"),
                ],

            ]

        ),

    )



@app.on_message(command(["غنيلي", "غني", "غ", "سبارك غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="💕 ¦ تـم اختيـار الصوره لـك",parse_mode="html",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
