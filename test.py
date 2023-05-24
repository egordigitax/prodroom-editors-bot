from PIL import Image

from core.services.posts import Post

image = Image.open('1840-11.jpeg')
Post.make_nerds(image, 'yellow', 'back_black').save('book_ready.png')
