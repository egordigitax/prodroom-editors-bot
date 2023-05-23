from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from PIL import Image


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