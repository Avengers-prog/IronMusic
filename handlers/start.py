# ππΌππΌπmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello π there! I can play music in voice chats of Telegeam Groups. I have a lot of cool feature that will amaze you!\n\nπ΄ Do you want me to play music in your Telegram groups'voice chats? Please click the \'π User Manual π\' button below to know how you can use me.\n\nπ΄ The Assistant must be in your group to play music in the voice chat of your group.\n\nπ΄ More info & commands mentioned in the [User Manual](https://telegra.ph/IΚα΄Ι΄Mα΄sΙͺα΄-05-31)\n\nA project by @I_AM_DIK""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π User Manual π", url="https://telegra.ph/IΚα΄Ι΄Mα΄sΙͺα΄-05-31")
                  ],[
                    InlineKeyboardButton(
                        "π¨βπ» Updates π¨βπ»", url="https://t.me/Ironman_updates"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Support Chat ποΈ", url="https://t.me/Iron_support"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**π΄ Music player is online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ποΈ Support Group ποΈ", url="https://t.me/Iron_support")
                ]
            ]
        )
   )

