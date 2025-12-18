from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8524129314:AAF5Tig7PktAhcaBhbwJV5I8FsV8-tGBVBk"

CHANNELS = [
    "@veideistoren",
    "@moneylootchanne",
    -1003582318168,
    -1003596647029
]

FINAL_LINK = "https://veideostores.netlify.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Join Channel 1", url="https://t.me/veideistoren")],
        [InlineKeyboardButton("Join Channel 2", url="https://t.me/moneylootchanne")],
        [InlineKeyboardButton("Join Channel 3", url="https://t.me/+LNG_kq6-UQhmNTI1")],
        [InlineKeyboardButton("Join Channel 4", url="https://t.me/+ZuFXqi_7XLc3YmVl")],
        [InlineKeyboardButton("✅ Submit", callback_data="check")]
    ]

    await update.message.reply_text(
        "🔒 Link paane ke liye pehle sabhi 4 channel join karo\n\n"
        "Join karne ke baad Submit dabao",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id

    for channel in CHANNELS:
        try:
            member = await context.bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                raise Exception
        except:
            await query.answer(
                "❌ Pehle sabhi channel join karo", show_alert=True
            )
            return

    await query.message.reply_text(
        f"✅ Verification successful!\n\n🎁 Tumhara link:\n{FINAL_LINK}"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(check, pattern="check"))
app.run_polling()
