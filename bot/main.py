from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
import logging

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

client_id = "929351d861394e70b4c2dd1e9cd524cb"
client_secret = "98ac1d6f78414a95af0ace7636575460"

def auth(client_id, client_secret):
    url = "https://accounts.spotify.com/api/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }

    r = requests.post(url, headers=headers, data=data)

    if r.status_code == 200:
        return r.json()["access_token"]
    else:
        print(f"HTTP {r.status_code} {r.text}")

access_token = auth(client_id, client_secret)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def album(update: Update, context: ContextTypes.DEFAULT_TYPE):
    id = context.args[0]
    url = f"https://api.spotify.com/v1/albums/{id}"
    headers = {"Authorization": f"Bearer {access_token}"}

    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        await context.bot.send_message(update.effective_user.id, res.json())
    else:
        await context.bot.send_message(update.effective_user.id, f"ERROR!\n{res.text}")


app = ApplicationBuilder().token("6277272735:AAFmp91lkMQ9tVpVzj5JoN8flGjgeV9MfJM").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("album", album))

app.run_polling()
