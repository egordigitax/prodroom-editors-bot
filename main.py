from typing import List

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from PIL import Image


async def send_message(update: Update, answer: str, buttons: List[List[str]], input_placeholder: str):
    await update.message.reply_text(answer, reply_markup=ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True, input_field_placeholder=input_placeholder
    ), )


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Оплатить", "Инструкция", "Помощь"]]
    await send_message(update, hello_answer, reply_keyboard, CHOOSE_ACTION)


def downloader(update, context):
    with open("temp/image.png", 'wb') as f:
        context.bot.get_file(update.message.document).download(out=f)
        img = Image.open('temp/image.png')
        logo = Image.open('logo.png')
        img.paste(logo, (img.width / 2 - logo.width / 2, img.height / 2 - logo.height / 2), logo)
        img.save('temp.png')



app = ApplicationBuilder().token("6224310851:AAFx-_V-5R60l6jeqH-r1E74vTBIPhHSk14").build()

app.add_handler(MessageHandler(filters.ATTACHMENT, downloader))

app.run_polling()