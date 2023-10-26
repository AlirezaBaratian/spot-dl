from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello")


app = ApplicationBuilder().token("6821812844:AAGkqrTx3Jg1nDbL1E6d-agg6qZ9Djjg1do").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()