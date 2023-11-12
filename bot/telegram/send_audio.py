from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_audio("./Rick Astley - Never Gonna Give You Up (Official Music Video) [dQw4w9WgXcQ].m4a")


app = ApplicationBuilder().token("6792755901:AAFEtxFHrzcRjsC1ENspvxOv5TuJaM0Ohrg").build()

app.add_handler(CommandHandler("start", start))

app.run_polling()