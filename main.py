from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

AUTO_COMMENT = """💎 Premium
👤 Admin: @RF_shakhr
📞 Telefon: +998 91 778 26 81

Buyurtma uchun admin bilan bog‘laning ✨"""

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message
    user = update.effective_user

    if msg and user:
        if user.id == OWNER_ID:
            await msg.reply_text(AUTO_COMMENT)

app = ApplicationBuilder().token(TOKEN).build()

# ❗ eng stabil variant
app.add_handler(MessageHandler(filters.ALL, handle))

print("Bot ishlayapti...")

app.run_polling()
