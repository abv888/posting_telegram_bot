import asyncio
import os

import uvloop

from aiogram import F, types
from aiogram.filters import Command

from sqlalchemy.ext.asyncio import AsyncSession

from models import Admin
from orm_query import orm_add_admin, orm_get_admin, orm_update_admin, orm_delete_admin
from utils import clone

from aiogram import Bot, Dispatcher
from pyrogram import Client
import telebot

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from bot_commands_list import admin_commands
from db import DataBaseSession
from engine import drop_db, create_db, session_maker


API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CLIENT_BOT_TOKEN = os.getenv("CLIENT_BOT_TOKEN")

CHANNEL_FROM = int(os.getenv("CHANNEL_FROM"))
CHANNEL_TO = int(os.getenv("CHANNEL_TO"))
TEST_CHANNEL_FROM = int(os.getenv("TEST_CHANNEL_FROM"))
TEST_CHANNEL_TO = int(os.getenv("TEST_CHANNEL_TO"))

PROMO_CODE = os.getenv("PROMO_CODE")
ADMIN_NAME = os.getenv("ADMIN_NAME")
MINES_BOT=os.getenv("MINES_BOT")
BRAWL_PIRATES_BOT=os.getenv("BRAWL_PIRATES_BOT")
COIN_FLIP_BOT=os.getenv("COIN_FLIP_BOT")
REVIEWS_CHANNEL=os.getenv("REVIEWS_CHANNEL")
LIVE_CHANNEL=os.getenv("LIVE_CHANNEL")

client = Client(
    name='session_client',
    api_id=API_ID,
    api_hash=API_HASH
)

client_bot = telebot.TeleBot(CLIENT_BOT_TOKEN)

bot = Bot(token=os.getenv("BOT_TOKEN"))

dp = Dispatcher()


@dp.message(Command('start'))
async def start(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
        if (message.from_user.username == "svr88888888") or (message.from_user.username == "yee7777777"):
            await orm_add_admin(
                session=session,
                admin=Admin(
                    telegram_id=message.from_user.id,
                    full_name=message.from_user.full_name,
                    username=message.from_user.username
                )
            )
    else:
        if admin.telegram_id is None:
            await orm_update_admin(
                session=session,
                admin=Admin(
                    telegram_id=message.from_user.id,
                    full_name=message.from_user.full_name,
                    username=message.from_user.username
                )
            )
            await bot.send_message(
                message.from_user.id,
                text='Добро пожаловать в бота!'
            )
        else:
            await bot.send_message(
                message.from_user.id,
                text='Добро пожаловать в бота!'
            )


@dp.message(Command('test'))
async def test(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        await clone(
            from_channel=TEST_CHANNEL_FROM,
            to_channel=TEST_CHANNEL_TO,
            bot=client_bot,
            client=client,
            admin_account=ADMIN_NAME,
            promocode=PROMO_CODE,
            reviews_channel=REVIEWS_CHANNEL,
            mines_bot=MINES_BOT,
            brawl_bot=BRAWL_PIRATES_BOT,
            coin_bot=COIN_FLIP_BOT,
            live_channel=LIVE_CHANNEL
        )


@dp.message(F.text.contains('test x'))
async def test_x(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        limit = int(message.text.split('test x')[1])
        await clone(
            from_channel=TEST_CHANNEL_FROM,
            to_channel=TEST_CHANNEL_TO,
            bot=client_bot,
            client=client,
            admin_account=ADMIN_NAME,
            promocode=PROMO_CODE,
            reviews_channel=REVIEWS_CHANNEL,
            mines_bot=MINES_BOT,
            brawl_bot=BRAWL_PIRATES_BOT,
            coin_bot=COIN_FLIP_BOT,
            live_channel=LIVE_CHANNEL,
            messages_limit=limit
        )


@dp.message(Command('post'))
async def post(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        await clone(
            from_channel=CHANNEL_FROM,
            to_channel=CHANNEL_TO,
            bot=client_bot,
            client=client,
            admin_account=ADMIN_NAME,
            promocode=PROMO_CODE,
            reviews_channel=REVIEWS_CHANNEL,
            mines_bot=MINES_BOT,
            brawl_bot=BRAWL_PIRATES_BOT,
            coin_bot=COIN_FLIP_BOT,
            live_channel=LIVE_CHANNEL
        )


@dp.message(F.text.contains('post x'))
async def post_x(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        limit = int(message.text.split('post x')[1])
        await clone(
            from_channel=CHANNEL_FROM,
            to_channel=CHANNEL_TO,
            bot=client_bot,
            client=client,
            admin_account=ADMIN_NAME,
            promocode=PROMO_CODE,
            reviews_channel=REVIEWS_CHANNEL,
            mines_bot=MINES_BOT,
            brawl_bot=BRAWL_PIRATES_BOT,
            coin_bot=COIN_FLIP_BOT,
            live_channel=LIVE_CHANNEL,
            messages_limit=limit
        )


@dp.message(F.text.contains('post from '))
async def post_from(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        global CHANNEL_FROM
        channel_from = int(message.text.split('post from ')[1])
        CHANNEL_FROM = channel_from


@dp.message(F.text.contains('test from '))
async def test_from(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        global TEST_CHANNEL_FROM
        test_channel_from = int(message.text.split('test from ')[1])
        TEST_CHANNEL_FROM = test_channel_from


@dp.message(F.text.contains('post to '))
async def post_to(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        global CHANNEL_TO
        channel_to = int(message.text.split('to ')[1])
        CHANNEL_TO = channel_to


@dp.message(F.text.contains('test to '))
async def test_to(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        global TEST_CHANNEL_TO
        test_channel_to = int(message.text.split('test to ')[1])
        TEST_CHANNEL_TO = test_channel_to


@dp.message(Command('add_admin'))
async def add_admin(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Для добавления администратора введите username в формате 'add @username'"
        )


@dp.message(F.text.contains("add @"))
async def get_add_username_handler(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        username_to_add = message.text.split('add @')[1]
        await orm_add_admin(
            session=session,
            admin=Admin(
                full_name=None,
                username=username_to_add,
                telegram_id=None
            )
        )


@dp.message(Command('delete_admin'))
async def delete_admin(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Для удаления администратора введите username в формате 'delete @username'"
        )


@dp.message(F.text.contains("delete @"))
async def get_delete_username_handler(
        message: types.Message,
        session: AsyncSession
):
    admin = await orm_get_admin(
        session=session,
        username=message.from_user.username
    )
    if admin is None:
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Нет доступа"
        )
    else:
        username_to_delete = message.text.split('delete @')[1]
        await orm_delete_admin(
            session=session,
            username=username_to_delete
        )


@dp.message(Command('help'))
async def help_handler(message: types.Message):
    await message.answer(text="/start - Запустить бота \n"
                              "/add_admin - Добавть администратора \n"
                              "/delete_admin - Удалить администратора \n"
                              "/post - Запостить 1 пост в основной канал \n"
                              "/test - Запостить 1 пост в тестовый канал \n"
                              "post x{количество постов} - Запостить x постов в основной канал \n"
                              "test x{количество постов} - Запостить x постов в тестовый канал \n"
                              "post from {ID канала} - Изменить тестовый канал для копирования \n"
                              "post to {ID канала} - Изменить основной канал для публикации \n"
                              "test from {ID канала} - Изменить тестовый канал для копирования \n"
                              "test to {ID канала} - Изменить тестовый канал для публикации \n"
                              "/help - Вывести памятку по использованию бота"
                         )


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()

    await create_db()


async def on_shutdown(bot):
    print('Bot shut down...')


async def main():
    await client.start()

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=admin_commands)
    await dp.start_polling(bot)
    await client_bot.polling()

uvloop.install()
asyncio.run(main())
