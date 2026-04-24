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
    msg = update.effective_message
    user = update.effective_user

    # faqat guruhda ishlaydi
    if update.effective_chat.type in ["group", "supergroup"]:
        if user and user.id == OWNER_ID:
            await msg.reply_text(AUTO_COMMENT)

app = ApplicationBuilder().token(TOKEN).build()

# ❗ MUHIM: text filter qo‘shildi
app.add_handler(MessageHandler(filters.TEXT, handle))

print("Bot ishlayapti...")

app.run_polling()
