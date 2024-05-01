import requests 
import os
import random
from dotenv import load_dotenv
import telegram


def downloading_a_comic_book(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(path, 'wb') as file:
      file.write(response.content)


def get_count_comic():
    url = "https://xkcd.com//info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    number = data["num"]
    return number


def get_comment():
    url = f"https://xkcd.com/{random.randint(1, get_count_comic())}/info.0.json"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    comment = data["alt"]
    title = data["title"]
    comic_url = data["img"]
    downloading_a_comic_book(comic_url, f"{title}.png")
    return comment, title


def upload_comic(token_tg, tg_chat_id):
    comment, title = get_comment()
    bot = telegram.Bot(token=token_tg)
    with open(f"{title}.png", "rb") as f:
      bot.send_document(chat_id=tg_chat_id, document=f, caption=comment)
    os.remove(f"{title}.png")


def main():
    load_dotenv() 
    tg_chat_id = os.environ["TG_CHAT_ID"]
    token_tg = os.environ["TOKEN_TG"]
    upload_comic(token_tg, tg_chat_id)

if __name__ == '__main__':
    main()