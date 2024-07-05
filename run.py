from os import getenv
import logging, sys, asyncio


from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from aiogram.fsm.storage.base import DefaultKeyBuilder

from aiogram_dialog import setup_dialogs


from app.start import linker


storage = RedisStorage.from_url('redis://localhost:6379/0',
                                key_builder=DefaultKeyBuilder(with_destiny=True))

load_dotenv()
bot = Bot(token=getenv('QUIZBOT_TOKEN'))

dp = Dispatcher(storage=storage)
dp.include_router(linker)

setup_dialogs(dp)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        dp.run_polling(bot)
    except KeyboardInterrupt:
        print('exit')