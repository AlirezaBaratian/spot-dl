from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

def login(client_id, client_secret):
    url = 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("6277272735:AAFmp91lkMQ9tVpVzj5JoN8flGjgeV9MfJM").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()