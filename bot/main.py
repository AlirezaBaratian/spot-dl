from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests
import logging
from dotenv import load_dotenv
import os
import auth
import yt_dlp

load_dotenv()

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


access_token = auth.auth()

commands: list = ["🎧 Preview Music"]

main_menu: list = [commands]

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

def get_info(id: str) -> bool | dict:
    global access_token
    url: str = f"https://api.spotify.com/v1/tracks/{id}"
    headers: dict = {
        "Authorization": f"Bearer {access_token}"
    }

    r = requests.get(url=url, headers=headers)

    if r.status_code == 200:
        return r.json()
    elif r.status_code == 401:
        access_token = auth.auth()
        get_info(id)
    else:
        return False
    
def parse_track_data(track_data: dict)-> dict:
    return {
        "name": track_data["name"],
        "artist": track_data["artists"][0]["name"],
        "album": track_data["album"]["name"],
        "image": track_data["album"]["images"][0]["url"],
        "id": track_data["id"],
        "release_date": track_data["album"]["release_date"],
        "duration": track_data["duration_ms"],
        "preview_url": track_data["preview_url"]
    }

def downlaod_audio(url: str) -> str:

    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'm4a',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        # Get the downloaded file name from the info_dict
        downloaded_file_name = info_dict['title'] + '.m4a'
        print(f"Downloaded: {downloaded_file_name}")
        return downloaded_file_name

async def send_track_info(update: Update, context: ContextTypes.DEFAULT_TYPE, track_data: dict ={}) -> None:
    title: str = track_data["name"]
    artist: str = track_data["artist"]
    album: str = track_data["album"]
    photo_url: str = track_data["image"]
    realese_date: str = track_data["release_date"]
    duration_minutes: int = int((int(track_data["duration"]) / 1000) // 60)
    duration_seconds: int = int(int(track_data["duration"]) / 1000 % 60)
    id: str = track_data["id"]
    youtube_url: str = f"https://youtube.com/watch?v={serach_youtube(artist, title)}"

    await update.message.reply_photo(photo_url, caption=f"""
🎧 Title: <b>{title}</b>
🎤 Artist: <b>{artist}</b> 
💿 Album: <b>{album}</b>
🚀 Release Date: <code>{realese_date}</code>
⏱ Duration: <b>{duration_minutes}m {duration_seconds}s</b>
🆔 ID: <code>{id}</code>
▶️ YouTube URL: {youtube_url}
""", parse_mode="HTML", reply_markup=ReplyKeyboardMarkup(main_menu, True, True, False, "Select an option:", False))

async def send_audio_preview(update: Update, context: ContextTypes.DEFAULT_TYPE, preview_url: str):
    caption: str = "🎤 Here's a preview."
    await update.message.reply_voice(preview_url, caption=caption, reply_markup=ReplyKeyboardMarkup(main_menu, True, True, False, "Select an option:", False))

def serach_youtube(artist: str, title: str) -> str:
    url: str = "https://www.googleapis.com/youtube/v3/search"
    api_key: str = os.getenv("YOUTUBE_API_KEY")
    qeury: str = f"{artist} {title}"

    params = {
        "key": api_key,
        "part": "snippet",
        "q": qeury,
        "maxResults": 5
    }

    r = requests.get(url, params=params)
    
    if r.status_code == 200:
        return r.json()["items"][0]["id"]["videoId"]

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text: str = update.message.text

    if text.startswith("https://"):
        url: str = text
        id:str = get_id(url)

        if not get_info(id):
            await send_error(update, context)
        else:
            track_data: dict = parse_track_data(get_info(id))
            await send_track_info(update, context, track_data=track_data)
            await send_audio_preview(update, context, preview_url=track_data["preview_url"])
    else:
        if text == commands[0]:
            await get_url_prompt(update, context)
        else:
            await wrong_text(update, context)

bot_token: str = os.getenv("BOT_TOKEN")
app = ApplicationBuilder().token(bot_token).build()

app = ApplicationBuilder().token(bot_token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT &  ~filters.COMMAND, handle_text))

app.run_polling()
