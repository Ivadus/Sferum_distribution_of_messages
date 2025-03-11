import logging
import requests
from vk.methods import get_credentials, get_user_credentials, get_message, send_message
from vk.types import Message, EventMessage
import asyncio


async def main(server, key, ts, vk_chat_ids, access_token, cookie, pts):
    print(f"Всего chat_id: {len(vk_chat_ids)}")
    print("Отправка сообщений...")
    for chat_id in vk_chat_ids:
        try:
            send_message(
                access_token,
                chat_id,
                "Тестовое сообщение, написанное от бота" #Сюда пишется сообщение, которое вы хотите разослать
            )
            await asyncio.sleep(1)
        except Exception as e:
            logging.exception(f"Ошибка при отправке сообщения в чат {chat_id}: {e}")
    print("Сообщения отправлены!")