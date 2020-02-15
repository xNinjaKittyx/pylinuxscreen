# PyLinuxScreen

This is just a simple script for my personal use. Anyone else is welcome to use it as well.

## How it works

This script will simply take an image from the clipboard, convert it to PIL, convert to bytes, then upload it to backblaze.

I follow the steps [here](https://jross.me/free-personal-image-hosting-with-backblaze-b2-and-cloudflare-workers/) in order to set it up with cloudflare.

Definitely things could be improved, but I'm too lazy to make it any better unless there's a convenient reason to do so.

## Why?

I wanted ShareX on linux, but that's not gonna happen. 
Sharenix doesn't do auth, and other screenshot tools I didn't want to be bothered with (terrible docs, terrible workflow, etc).

## Installation

```
git clone https://github.com/xNinjaKittyx/pylinuxscreen.git
cd pylinuxscreen
poetry install
poetry run python b2upload.py
```

## Configuration

You need to create a toml file in the same folder name config.toml with these details
```
bucket_name = ""  # Name of b2 bucket
app_key_id = ""  # App Key ID for bucket
app_key = ""  # App Key for bucket
custom_url = ""  # The URL you want it to post the image with
```
