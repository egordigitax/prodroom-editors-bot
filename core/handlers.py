import os
import uuid
from typing import List

from PIL import Image
from telegram import Update, ReplyKeyboardMarkup, InputMediaPhoto
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

from core.services.posts import Post

user_actions = {}


def get_handlers():
    return [
        CommandHandler("start", hello),
        MessageHandler(filters.Regex("Ремайндер"), reminder),
        MessageHandler(filters.Regex("Мемы"), memes),
        MessageHandler(filters.Regex("Литература"), books),
        MessageHandler(filters.Regex("История жанров"), history),
        MessageHandler(filters.Regex("For Nerds"), nerds),
        MessageHandler(filters.Regex("О наболевшем"), pain),
        MessageHandler(filters.Regex("Плагины"), plugins),
        MessageHandler(filters.Regex("Вредные советы"), advice),
        MessageHandler(filters.ATTACHMENT, posts_factory)
    ]


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'hello')
    await send_message(update, 'Привет!', reply_keyboard, 'Давай сделаем пост')

async def reminder(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'reminder')
    await send_message(update, 'Отправь картинку документом. В идеале - 1500х1500 пикселей.', reply_keyboard, 'Жду картинку')

async def memes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'memes')
    await send_message(update, 'Отправь картинку документом. В идеале - 1500х1500 пикселей.', reply_keyboard, 'Жду картинку')

async def books(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'books')
    await send_message(update, 'Отправь картинку документом. В идеале - 640x900 пикселей.', reply_keyboard, 'Жду картинку')

async def history(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'history')
    await send_message(update, 'Отправь картинку документом. В идеале - 1500х1500 пикселей.', reply_keyboard, 'Жду картинку')

async def nerds(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'nerds')
    await send_message(update, 'Отправь картинку документом. В идеале - 1500х1500 пикселей.', reply_keyboard, 'Жду картинку')

async def pain(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'pain')
    await send_message(update, 'Отправь картинку документом. В идеале - 1500х1500 пикселей.', reply_keyboard, 'Жду картинку')

async def plugins(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'plugins')
    await send_message(update, 'Отправь картинку документом. В идеале - 1500х1500 пикселей.', reply_keyboard, 'Жду картинку')

async def advice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    reply_keyboard = [["Ремайндер", "Мемы", "Литература", "История жанров", "For Nerds", "О наболевшем", "Плагины", "Вредные советы"]]
    set_status(update.effective_user.username, 'advice')
    await send_message(update, 'Отправь картинку документом. В идеале - 1500х1500 пикселей.', reply_keyboard, 'Жду картинку')

async def posts_factory(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user.username
    if user in user_actions.keys():

        if user_actions[user] == 'reminder':
            img = await downloader(update, context)
            post = Post.make_reminder(img, "green", "back_white")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

        if user_actions[user] == 'memes':
            img = await downloader(update, context)
            post = Post.make_memes(img, "green")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

        if user_actions[user] == 'books':
            img = await downloader(update, context)
            post = Post.make_books(img, "green")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

        if user_actions[user] == 'history':
            img = await downloader(update, context)
            post = Post.make_history(img, "green", "back_white")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

        if user_actions[user] == 'nerds':
            img = await downloader(update, context)
            post = Post.make_nerds(img, "yellow", "back_white")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

        if user_actions[user] == 'pain':
            img = await downloader(update, context)
            post = Post.make_pain(img, "green")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

        if user_actions[user] == 'plugins':
            img = await downloader(update, context)
            post = Post.make_plugins(img, "green", "back_white")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

        if user_actions[user] == 'advice':
            img = await downloader(update, context)
            post = Post.make_advice(img, "green")
            post_uuid = str(uuid.uuid4())
            post.save(f'temp/{post_uuid}.png')
            await send_document(update, context, f'temp/{post_uuid}.png')

    set_status(user, 'hello')


async def downloader(update, context):
    _uuid = str(uuid.uuid4())
    file = await context.bot.get_file(update.message.document)
    await file.download_to_drive(f'temp/{_uuid}.png')
    img = Image.open(f'temp/{_uuid}.png')
    os.remove(f'temp/{_uuid}.png')
    return img


async def send_message(update: Update, answer: str, buttons: List[List[str]], input_placeholder: str):
    await update.message.reply_text(answer, reply_markup=ReplyKeyboardMarkup(
        buttons, one_time_keyboard=True, input_field_placeholder=input_placeholder, resize_keyboard=True
    ), )

async def send_document(update, context, image_path):
    with open(image_path, "rb") as file:
        await context.bot.send_document(update.message.chat_id, file)


def set_status(user, status):
    user_actions.update({user: status})
