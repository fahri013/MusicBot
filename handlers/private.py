from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Dear {message.from_user.first_name}!

😁 Aku Ardhito Bot musik

🥳 Bisako Putar musik di grup Telegram Voice Chat mu😉

Pengembang by ⚡ @papirocknroll⚡

My commands - type  /help to get commands, which work in grp

Terima kasih bro.

Regrards [AREASULAWESI](https://t.me/AREASULAWESI)
**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 DEPLOY LINK🛠", url="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fkartikrajofficial%2FMusicBot&template=https%3A%2F%2Fgithub.com%2Fkartikrajofficial%2FMusicBot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/AREASULAWESI "
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/AREA_SULAWESI "
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/Kingbot_Music_Bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**⭐ARDHITO MUSIC PLAYER IS ALWAYS ACTIVE!!⭐**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/AREA_SULAWESI")
                ]
            ]
        )
   )
