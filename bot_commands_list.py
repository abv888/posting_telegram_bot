from aiogram.types import BotCommand

admin_commands = [
    BotCommand(
        command='start',
        description='Запустить бота'
    ),
    BotCommand(
        command='help',
        description='Помощь'
    ),
    BotCommand(
        command='adduser',
        description='Добавить нового члена совета директоров'
    ),
    BotCommand(
        command='new',
        description='Добавить документ на согласование'
    ),
    BotCommand(
        command='status',
        description='Статус по текущему согласованию'
    )
]