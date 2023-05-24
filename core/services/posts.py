from typing import List

import numpy
from PIL import Image
from blend_modes import screen
import numpy as np
from core.services.exceptions import BadImageSizeError, ImageCountError


class Post:

    @staticmethod
    def make_advice(image: Image.Image, color: str):
        try:
            sticker = Image.open(f'core/services/sources/advice/{color}.png')
        except Exception:
            raise FileNotFoundError
        back = Post.resize_to_square(image)
        back.paste(sticker, (0, 0), sticker)
        return back

    @staticmethod
    def make_books(image: Image.Image, color: str):

        if image.width < 650 or image.height < 900 or image.height < image.width:
            raise BadImageSizeError

        width_divide = 650 / image.width
        image_rescaled = image.resize((int(image.width * width_divide),
                                       int(image.height * width_divide)))

        try:
            back = Image.open('core/services/sources/books/back.png')
            mask = Image.open('core/services/sources/books/mask.png')
            overlay = Image.open('core/services/sources/books/overlay.png')
            sticker = Image.open(f'core/services/sources/books/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        book = Image.new('RGBA', (1500, 1500), (0, 0, 0, 0))
        book.paste(image_rescaled, (425, 300))

        back.paste(book, (0, 0), mask)
        back = screen(np.array(back).astype(float), np.array(overlay).astype(float), 1)
        back = Image.fromarray(np.uint8(back))
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def make_history(image: Image.Image, color: str, back_color: str):
        try:
            back = Image.open(f'core/services/sources/history/{back_color}.png')
            mask = Image.open(f'core/services/sources/history/mask.png')
            sticker = Image.open(f'core/services/sources/history/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        back.paste(Post.resize_to_square(image), (0, 0), mask)
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def make_nerds(image: Image.Image, color: str, back_color: str):
        try:
            back = Image.open(f'core/services/sources/nerds/{back_color}.png')
            mask = Image.open(f'core/services/sources/nerds/mask.png')
            sticker = Image.open(f'core/services/sources/nerds/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        back.paste(Post.resize_to_square(image), (0, 0), mask)
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def make_plugins(image: Image.Image, color: str, back_color: str):
        try:
            back = Image.open(f'core/services/sources/plugins/{back_color}.png')
            mask = Image.open(f'core/services/sources/plugins/mask.png')
            sticker = Image.open(f'core/services/sources/plugins/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        back.paste(Post.resize_to_square(image), (0, 0), mask)
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def make_reminder(image: Image.Image, color: str, back_color: str):
        try:
            back = Image.open(f'core/services/sources/reminder/{back_color}.png')
            mask = Image.open(f'core/services/sources/reminder/mask.png')
            sticker = Image.open(f'core/services/sources/reminder/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        back.paste(Post.resize_to_square(image), (0, 0), mask)
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def make_memes(image: Image.Image, color: str):
        try:
            sticker = Image.open(f'core/services/sources/reminder/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        back = Post.resize_to_square(image)
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def make_pain(image: Image.Image, color: str):
        try:
            sticker = Image.open(f'core/services/sources/reminder/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        back = Post.resize_to_square(image)
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def make_weekly(images: List[Image.Image], color: str):

        back = None

        if len(images) != 3 or len(images) != 9:
            raise ImageCountError

        if len(images) == 3:
            back = Image.new('RGBA', (1500, 550), (255, 255, 255, 255))
        if len(images) == 9:
            back = Image.new('RGBA', (1500, 1500), (255, 255, 255, 255))

        for index, image in enumerate(images):
            resized = image.resize((438, 438))
            row = 0

        try:
            sticker = Image.open(f'core/services/sources/reminder/stickers/{color}.png')
        except Exception:
            raise FileNotFoundError

        back = Post.resize_to_square(image)
        back.paste(sticker, (0, 0), sticker)

        return back

    @staticmethod
    def resize_to_square(image: Image.Image):
        new_image = None
        if image.width == image.height:
            new_image = image.resize((1500, 1500))
        if image.width > image.height:
            height_divide = 1500 / image.height
            new_image = image.resize((int(image.width * height_divide),
                          int(image.height * height_divide)))
        if image.width < image.height:
            width_divide = 1500 / image.width
            new_image = image.resize((int(image.width * width_divide),
                          int(image.height * width_divide)))

        print(new_image.width)
        print(new_image.height)
        crop_width = int((new_image.width - 1500) / 2)
        crop_height = int((new_image.height - 1500) / 2)
        cropped = new_image.crop((crop_width, crop_height, crop_width+1500, crop_height+1500))
        return cropped
