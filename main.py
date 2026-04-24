from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

AUTO_COMMENT = """💎 Premium
👤 Admin: @RF_shakhr
📞 Telefon: +998 91 778 26 81

Buyurtma uchun admin bilan bog‘laning ✨"""

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message

    if msg:
        try:
            await msg.reply_text(AUTO_COMMENT)
        except Exception as e:
            print("Xatolik:", e)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, handle))

print("✅ Bot ishlayapti...")

app.run_polling()
