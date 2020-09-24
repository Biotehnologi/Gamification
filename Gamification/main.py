# -*- coding: utf-8 -*-
import asyncio

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN, PROXY_URL

loop = asyncio.get_event_loop()
bot = Bot(API_TOKEN, parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

if __name__ == '__main__':
    from handlers import *
    executor.start_polling(dp, on_startup=send_to_admin,  skip_updates=True)
