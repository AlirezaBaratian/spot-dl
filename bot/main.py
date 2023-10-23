from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests
import logging
from typing import Dict
from dotenv import load_dotenv
import os

load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

access_token = "BQCzkUXYzKs7Jev9vAlm1ts64HW3vig3Hj5yv3IaThpVOtnmXVtvtspj--ohvIAc7v34P1w7bZhYrYLP92yvwjJuL9MTMMVIO_URe6E3m_MkjgVWyXI"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    first_name = update.effective_user.first_name

    await update.message.reply_text(text=f"🤗 Welcome, {first_name}!", reply_to_message_id=update.message.message_id, reply_markup=ReplyKeyboardMarkup([["About", "Contact", "Guide", "Get Music Data"]], True, True, False, "Select an option:", False))

async def wrong_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="⛔️ Wrong message!")

def get_id(url: str) -> str:
    url_list: list = url.split("://")[1].split("/")
    type: str = url_list[1]
    id: str = url_list[2]
    return id

def get_info(str: id) -> None:
    url: str = f"https://api.spotify.com/v1/tracks/{id}"
    headers: Dict = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    print(f'HTTP {r.status_code} {r.text}')

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text: str = update.message.text

    if text.startswith("https://"):
        url: str = text
        id:str = get_id(url)
        get_info(id)
    else:
        await wrong_text(update, context)

bot_token: str = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT &  ~filters.COMMAND, handle_text))

app.run_polling()
