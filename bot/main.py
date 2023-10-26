from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests
import logging
from dotenv import load_dotenv
import os
from typing import Dict, List
import auth

load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


access_token = auth.auth()

main_menu: List = [["🪀 Get Music Data"]]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    first_name = update.effective_user.first_name

    await update.message.reply_text(text=f"🤗 Welcome, {first_name}!", reply_to_message_id=update.message.message_id, reply_markup=ReplyKeyboardMarkup(main_menu, True, True, False, "Select an option:", False))

async def wrong_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="⛔️ Wrong message!")

async def send_error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="⚠️ An error occured!\n↘️ Try again.")

async def get_url_prompt(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text="🧢 Send me a Spotify track url. \n🖇 Example: https://open.spotify.com/track/4cOdK2wGLETKBW3PvgPWqT?si=2edaedb9ac174e94", disable_web_page_preview=True)

def get_id(url: str) -> str:
    url_list: list = url.split("://")[1].split("/")
    id: str = url_list[2].split("?")[0]
    return id

def get_info(id: str) -> bool | Dict:
    global access_token
    url: str = f"https://api.spotify.com/v1/tracks/{id}"
    headers: Dict = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    if r.status_code == 200:
        return r.json()
    elif r.status_code == 401:
        access_token = auth.auth()
        auth.refresh_token(access_token)
        get_info(id)
    else:
        return False
    
def parse_track_data(track_data: Dict)-> Dict:
    return {
        "name": track_data["name"],
        "artist": track_data["artists"][0]["name"],
        "album": track_data["album"]["name"],
        "image": track_data["album"]["images"][0]["url"],
        "id": track_data["id"],
        "rank": track_data["popularity"],
        "duration": track_data["duration_ms"],
        "preview_url": track_data["preview_url"]
    }

async def send_track_info(update: Update, context: ContextTypes.DEFAULT_TYPE, track_data: Dict ={}) -> None:
    name: str = track_data["name"]
    artist: str = track_data["artist"]
    album: str = track_data["album"]
    photo_url: str = track_data["image"]
    rank: str = track_data["rank"]
    duration_minutes: int = int((int(track_data["duration"]) / 1000) // 60)
    duration_seconds: int = int(int(track_data["duration"]) / 1000 % 60)
    id: str = track_data["id"]
    preview_url: str = track_data["preview_url"]

    await update.message.reply_photo(photo_url, caption=f"""
🎧 Track: <b>{name}</b>
🎤 Artist: <b>{artist}</b> 
💿 Album: <b>{album}</b>
🏅 Rank: <b>{rank}</b>
⏱ Duration: <b></b>{duration_minutes}m, {duration_seconds}s
🆔 ID: <code>{id}</code>
""", parse_mode="HTML", reply_markup=ReplyKeyboardMarkup(main_menu, True, True, False, "Select an option:", False))
    await update.message.reply_voice(preview_url)

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text: str = update.message.text

    if text.startswith("https://"):
        url: str = text
        id:str = get_id(url)

        if not get_info(id):
            await send_error(update, context)
        else:
            await send_track_info(update, context, track_data=parse_track_data(get_info(id)))
    else:
        if text == "🪀 Get Music Data":
            await get_url_prompt(update, context)
        else:
            await wrong_text(update, context)

bot_token: str = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT &  ~filters.COMMAND, handle_text))

app.run_polling()
