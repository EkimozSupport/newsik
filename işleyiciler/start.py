from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(_expand_commands("start@MangoMusicalbot","start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""πΌπππππππ π±ππ ππππππππ πΆππππππΔ±πππ π±ππ πππππππ πΎππππππ πΌΓΌπ£ππ Γππππππππ’ππππ. πΆπππππππ£ππ πππππ ππππππππππ πΓΌπ£ππ Γ§πππππππππ πΓ§ππ π°ππππππΔ±π ππππππππ£ππ πππππΔ± πππππππ. π°πΔ°πππ°π½; @MissMuzikAsistan.""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π KullanΔ±m Bilgisi π", url="https://t.me/ucretlibotlar/18")
                  ],[
                    InlineKeyboardButton(
                        "π₯΅ MANGO ASΔ°STAN π₯΅", url="https://t.me/MangoMusicPlayer"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "π Γcretli Botlar ποΈ", url="https://t.me/UcretliBotlar"
                    )],
                [
                    InlineKeyboardButton(text= "πSahibimπ", url = "https://t.me/kizilsancaksahibi")
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command(_expand_commands("reload@Mangomusicalbot","reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Admin Listesi GΓΌnΓ§ellendi..β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Destek", url="https://t.me/MangoMusicalbot")
                ]
            ]
        )
   )
