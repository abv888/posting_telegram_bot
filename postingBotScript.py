import asyncio
import os

from aiogram import Bot, Dispatcher
from pyrogram import Client

from dotenv import load_dotenv, find_dotenv

from bot_commands_list import admin_commands
from db import DataBaseSession
from engine import drop_db, create_db, session_maker

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


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('Bot shut down...')


async def main():
    await client.start()
    await client_bot.start()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=admin_commands)
    await dp.start_polling(bot)

asyncio.run(main())
