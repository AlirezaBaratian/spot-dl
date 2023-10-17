from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name

    await update.message.reply_text(text=f"🤗 Welcome, {first_name}", reply_to_message_id=update.message.message_id, reply_markup=ReplyKeyboardMarkup([["About", "Contact", "Guide", "Get Music Data"]], True, True, False, "Select an option:", False))


app = ApplicationBuilder().token("6277272735:AAFmp91lkMQ9tVpVzj5JoN8flGjgeV9MfJM").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
