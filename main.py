from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import os

# ENV o'zgaruvchilar
TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))

# Avtomatik yoziladigan komment
AUTO_COMMENT = """💎 Premium
👤 Admin: @RF_shakhr
📞 Telefon: +998 91 778 26 81

Buyurtma uchun admin bilan bog‘laning ✨"""

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    user = update.effective_user

    # faqat o'zing yozgan xabarga ishlaydi
    if msg and user and user.id == OWNER_ID:
        try:
            await msg.reply_text(AUTO_COMMENT)
        except Exception as e:
            print("Xatolik:", e)

# Botni ishga tushirish
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, handle))

print("Bot ishga tushdi...")

app.run_polling()
