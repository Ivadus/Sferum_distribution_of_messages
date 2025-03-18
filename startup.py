import asyncio
import logging
from os import getenv
from dotenv import load_dotenv

from aiogram import Bot
from vk.methods import get_credentials, get_user_credentials
from main import main

load_dotenv()

logging.basicConfig(
    filename="./sferum_in.log",
    encoding="utf-8",
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p'
)

# В vk_chat_ids вы добавляете ID пользователей, которым хотите разослать сообщение.
# Я как администратор школы в Сферуме беру все ID скопом в отчете активности педагогов формата .csv
vk_chat_ids = [
    "000000001", "000000002", "000000003", "000000004", "000000005", "000000006"
]

# Перейдите по ссылке: Sferum >> Ctrl + Shift + C >> Приложение>> Хранилище>> Файлы cookie >> https://web.vk.me
# После этого вы должны увидеть таблицу со всеми файлами cookie с этого сайта
# Найдите remixdsid и скопируйте данные из столбца Cookie Value.
cookie = "Ваш куки"

user = get_user_credentials(cookie)
access_token = user.access_token
creds = get_credentials(access_token)

loop = asyncio.get_event_loop()

try:
    task2 = loop.create_task(main(
        creds.server,
        creds.key,
        creds.ts,
        vk_chat_ids,
        access_token,
        cookie,
        creds.pts
    ))

    logging.info("Loop starting")
    loop.run_forever()

except KeyboardInterrupt:
    pass
except Exception as e:
    logging.exception(e)
finally:
    logging.info("Closing loop...")
    loop.close()
    logging.info("Loop closed")
