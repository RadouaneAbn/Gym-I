#!/usr/bin/python3
from PIL import Image
from io import BytesIO
IMG_BB_TOKEN = "dfcbe0e16596fd0c2dbb83c94c90718b"
IMG_BB_URL = "https://api.imgbb.com/1/upload"
IMG_SIZE = (128, 128)

def resize_128(img_data):
    img = Image.open(BytesIO(img_data))
    img.thumbnail(IMG_SIZE, Image.Resampling.LANCZOS)

    resized_buffer = BytesIO()
    img.save(resized_buffer, format=img.format)
    resized_buffer.seek(0)
    return resized_buffer.getvalue()
