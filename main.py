from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

AUTO_COMMENT = """💎 Premium
👤 Admin: @RF_shakhr

Buyurtma uchun admin bilan bog‘laning ✨"""

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    user = update.effective_user

    if msg and user and user.id == OWNER_ID:
        await msg.reply_text(AUTO_COMMENT)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle))
app.run_polling()
