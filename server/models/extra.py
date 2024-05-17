#!/usr/bin/python3
from PIL import Image
from io import BytesIO
from os import getenv




def resize_128(img_data):
    img = Image.open(BytesIO(img_data))
    img.thumbnail(IMG_SIZE, Image.Resampling.LANCZOS)

    resized_buffer = BytesIO()
    img.save(resized_buffer, format=img.format)
    resized_buffer.seek(0)
    return resized_buffer.getvalue()
