import asyncio
import os

from aiogram import Bot, Dispatcher
from pyrogram import Client

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CLIENT_BOT_TOKEN = os.getenv("CLIENT_BOT_TOKEN")

CHANNEL_FROM = int(os.getenv("CHANEL_FROM"))
CHANNEL_TO = int(os.getenv("CHANEL_TO"))
TEST_CHANNEL_FROM = int(os.getenv("TEST_CHANEL_FROM"))
TEST_CHANNEL_TO = int(os.getenv("TEST_CHANEL_TO"))

client = Client(name='session_client', api_id=API_ID, api_hash=API_HASH)
client_bot = Client(name='session_bot', bot_token=CLIENT_BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

bot = Bot(token=BOT_TOKEN)

dp = Dispatcher()


async def main():
    await client.start()
    await client_bot.start()

    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.set_my_commands(commands=private)
    await dp.start_polling(bot)

asyncio.run(main())
