import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

TEXT = """💎 Premium
👤 Admin: @RF_shakhr
📞 Telefon: +998 91 778 26 81

Buyurtma uchun admin bilan bog‘laning ✨"""

async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.effective_user.id == OWNER_ID:
        await update.message.reply_text(TEXT)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, reply))

print("RUNNING...")

app.run_polling()
