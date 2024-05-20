#!/usr/bin/python3
""" This file contains some extra function that i used
    in the back-end
"""
from PIL import Image
from io import BytesIO
from os import getenv
import requests

IMG_BB_TOKEN = getenv("IMG_BB_TOKEN")
IMG_BB_URL = getenv("IMG_BB_URL")
IMG_SIZE = (128, 128)


def resize_128(img_data):
    """ This function resizes a image but keeps the original w-h """
    img = Image.open(BytesIO(img_data))
    img.thumbnail(IMG_SIZE, Image.Resampling.LANCZOS)

    resized_buffer = BytesIO()
    img.save(resized_buffer, format=img.format)
    resized_buffer.seek(0)
    return resized_buffer.getvalue()


def upload_picture(img):
    """ This fucntion uploads an image intp IMG BB web site """
    res = requests.post(IMG_BB_URL, files={"image": img},
                        data={"key": IMG_BB_TOKEN})
    return res.json()["data"]["display_url"]
