#!/usr/env/python3
import io
import secrets
import shlex
import subprocess
import time

import toml
import xxhash

import b2sdk.v1 as b2
import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk
from PIL import Image


clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)

image = None
# print("waiting for image")
while image is None:
    image = clipboard.wait_for_image()

# For some reason, grabbing the clipboard as soon as its available causes it to not get all the data.
image = clipboard.wait_for_image()

# print('got image')
len(image.get_pixels())
print((image.get_width(), image.get_height()))
pillow_image = Image.frombytes(
    "RGBA",
    (image.get_width(), image.get_height()),
    image.get_pixels()
)
fp = io.BytesIO()
pillow_image.save(fp, format="png")
fp.seek(0)
data = fp.read()
# print(type(data))
assert len(data) != 0, "There's no data... "

token_image_name = f"{xxhash.xxh64(data).hexdigest()}.png"

# preparing b2
config = toml.load(open('config.toml'))
info = b2.InMemoryAccountInfo()
api = b2.B2Api(info)
api.authorize_account("production", config['app_key_id'], config['app_key'])

bucket = api.get_bucket_by_name(config['bucket_name'])  
file_version = bucket.upload_bytes(
    data_bytes=data,
    file_name=token_image_name
)

# print(file_version.as_dict())
url = f"{config['custom_url']}{token_image_name}"
print(url)

subprocess.run(
    f"echo \"{url}\" | xclip -selection CLIPBOARD -r ",
    shell=True,
    check=True,
)
