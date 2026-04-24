import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = os.getenv("OWNER_ID")

# Tekshiruv
if not TOKEN:
    print("❌ BOT_TOKEN topilmadi")
    exit()

if not OWNER_ID:
    print("❌ OWNER_ID topilmadi")
    exit()

try:
    OWNER_ID = int(OWNER_ID)
except:
    print("❌ OWNER_ID noto‘g‘ri formatda")
    exit()

AUTO_COMMENT = """💎 Premium
👤 Admin: @RF_shakhr
📞 Telefon: +998 91 778 26 81

Buyurtma uchun admin bilan bog‘laning ✨"""

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message
    user = update.effective_user
    chat = update.effective_chat

    if (
        msg
        and user
        and user.id == OWNER_ID
        and chat.type != "private"
        and not msg.reply_to_message
    ):
        try:
            await msg.reply_text(AUTO_COMMENT)
        except Exception as e:
            print("Xatolik:", e)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, handle))

print("✅ Bot ishga tushdi")

app.run_polling()
