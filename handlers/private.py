from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters1)
async def start(_, message: Message):
    
    await message.reply_text(
        f"""**
🌠❰ǫᴜᴇᴇɴ✘ᴀʟɪsʜᴀ❱ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴀxᴇᴅ

sᴜᴘᴇʀғᴀsᴛ ᴀɴᴅ ʜɪɢʜ ǫᴜᴀʟɪᴛʏ ᴠᴄ ᴍᴜsɪᴄ

ᴘʟᴀʏᴇʀ ʙᴏᴛ ᴄʀᴇᴀᴛᴇᴅ ʙʏ [Aʙʜɪᴍᴀɴʏᴜ Sɪɴɢʜ Rᴀɴᴀᴡᴀᴛ](https://t.me/Venom_Hai_Hum)**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❰🅞︎𝘄🅝︎𝗲🅡︎❱", url="https://t.me/Venom_Hai_Hum")
                  ],[
                    InlineKeyboardButton(
                        "❰ᴀʟɪꜱʜᴀ✘ᴘʟᴀʏᴇʀ 𝔖ᴜᴘᴘᴏƦᴛ❱", url="https://t.me/Shayri_Music_Lovers"
                    ),
                    InlineKeyboardButton(
                        "❰ᴀʟɪꜱʜᴀ✘ᴘʟᴀʏᴇʀ ɢƦᴏᴜᴘ❱", url="https://t.me/AlishaSupport"
                    )
                ],
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("hexor") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**𝗠𝘂𝘀𝗶𝗰 𝗕𝗼𝘁 𝗢𝗻𝗹𝗶𝗻𝗲 𝗡𝗼𝘄\n🌠❰ᴀʟɪꜱʜᴀ✘ᴘʟᴀʏᴇʀ❱<3**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌼𝔖ᴜᴘᴘᴏƦᴛ", url="https://t.me/AlishaSupport")
                ]
            ]
        )
   )
