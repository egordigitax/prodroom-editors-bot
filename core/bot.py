from typing import List

from telegram.ext import ApplicationBuilder, MessageHandler, Application

from core.handlers import get_handlers


def start_bot(token: str):
    app = ApplicationBuilder().token("6224310851:AAFx-_V-5R60l6jeqH-r1E74vTBIPhHSk14").build()
    handlers = get_handlers()
    add_handlers(app, handlers)
    app.run_polling()


def add_handlers(app: Application, handlers_list: List[MessageHandler]):
    for handler in handlers_list:
        app.add_handler(handler)
