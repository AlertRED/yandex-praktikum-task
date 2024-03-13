import sys
import yaml
import logging
from aiogram import Dispatcher, types

import config
from bot.constants import COMMANDS_DESCRIPTION
from bot.middlewares import LoggerMiddleware
from bot.instances import (
    bot,
    dispatcher,
)


def __get_commands():
    return [
        types.BotCommand(
            command='/my_photos',
            description=COMMANDS_DESCRIPTION.get('/my_photos'),
        ),
        types.BotCommand(
            command='/my_hobbies',
            description=COMMANDS_DESCRIPTION.get('/my_hobbies'),
        ),
        types.BotCommand(
            command='/describe_me',
            description=COMMANDS_DESCRIPTION.get('/describe_me'),
        ),
    ]


def __setup_middlewares(dp: Dispatcher):
    logger_middleware = LoggerMiddleware(logger=logging.getLogger('bot'))
    dp.message.outer_middleware(logger_middleware)
    dp.callback_query.outer_middleware(logger_middleware)
    dp.poll_answer.outer_middleware(logger_middleware)


def __setup_logger():
    if config.IS_DEVELOP:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    else:
        with open(config.LOGGING_CONFIG_PATH, 'r') as f:
            config_d = yaml.safe_load(f.read())
            logging.config.dictConfig(config_d)


async def run():
    from bot import handlers

    __setup_logger()
    __setup_middlewares(dispatcher)

    await bot.set_my_commands(
        commands=__get_commands(),
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dispatcher.start_polling(bot)
