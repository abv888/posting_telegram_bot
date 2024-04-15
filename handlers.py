from aiogram import F, types
from aiogram.filters import Command


from utils import clone
import postingBotScript as p


@p.dp.message(Command('start'))
async def start(message: types.Message):
    await p.bot.send_message(message.from_user.id, text='Добро пожаловать в бота!')


@p.dp.message(Command('test'))
async def test(message: types.Message):
    await clone(
        from_channel=p.TEST_CHANNEL_FROM,
        to_channel=p.TEST_CHANNEL_TO,
        bot=p.client_bot,
        client=p.client
    )


@p.dp.message(F.text.contains('test '))
async def post(message: types.Message):
    limit = int(message.text.split('test ')[0])
    await clone(
        from_channel=p.TEST_CHANNEL_FROM,
        to_channel=p.TEST_CHANNEL_TO,
        bot=p.client_bot,
        client=p.client,
        messages_limit=limit
    )


@p.dp.message(Command('post'))
async def test(message: types.Message):
    await clone(
        from_channel=p.CHANNEL_FROM,
        to_channel=p.CHANNEL_TO,
        bot=p.client_bot,
        client=p.client
    )


@p.dp.message(F.text.contains('post '))
async def post(message: types.Message):
    limit = int(message.text.split('post ')[0])
    await clone(
        from_channel=p.CHANNEL_FROM,
        to_channel=p.CHANNEL_TO,
        bot=p.client_bot,
        client=p.client,
        messages_limit=limit
    )


@p.dp.message(F.text.contains('from '))
async def post(message: types.Message):
    channel_from = int(message.text.split('from ')[0])
    p.CHANNEL_FROM = channel_from


@p.dp.message(F.text.contains('test from '))
async def post(message: types.Message):
    test_channel_from = int(message.text.split('from ')[0])
    p.TEST_CHANNEL_FROM = test_channel_from


@p.dp.message(F.text.contains('to '))
async def post(message: types.Message):
    channel_to = int(message.text.split('to ')[0])
    p.CHANNEL_TO = channel_to


@p.dp.message(Command('add_admin'))
async def add_admin(message: types.Message):
    ...


@p.dp.message(F.text.contains("add @"))
async def get_username_handler(message: types.Message):
    ...


@p.dp.message(Command('delete_admin'))
async def add_admin(message: types.Message):
    ...


@p.dp.message(F.text.contains("delete @"))
async def get_username_handler(message: types.Message):
    ...
