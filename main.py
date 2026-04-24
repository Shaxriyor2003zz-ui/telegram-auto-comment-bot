import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")

TEXT = """premium
admin @RF_shakhr
telefon +998 91 778 26 81
"""

async def handle_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.channel_post:
        try:
            await context.bot.send_message(
                chat_id=update.channel_post.chat_id,
                text=TEXT,
                reply_to_message_id=update.channel_post.message_id
            )
        except Exception as e:
            print(e)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, handle_post))

app.run_polling()
