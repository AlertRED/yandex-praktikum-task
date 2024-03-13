from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

import config


bot = Bot(
    token=config.API_TOKEN,
    parse_mode='HTML',
)

dispatcher = Dispatcher(storage=MemoryStorage())
