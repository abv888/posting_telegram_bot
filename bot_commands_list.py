from aiogram.types import BotCommand

admin_commands = [
    BotCommand(
        command='start',
        description='Запустить бота'
    ),
    BotCommand(
        command='add_admin',
        description='Добавть администратора'
    ),
    BotCommand(
        command='delete_admin',
        description='Удалить администратора'
    ),
    BotCommand(
        command='post',
        description='Запостить 1 пост в основной канал'
    ),
    BotCommand(
        command='test',
        description='Запостить 1 пост в тестовый канал'
    )
,
    BotCommand(
        command='help',
        description='Вывести памятку по использованию бота'
    )
]