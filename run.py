from os import getenv
import logging, sys

from dotenv import load_dotenv

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from app.start import router


storage = MemoryStorage()

load_dotenv()
bot = Bot(token=getenv('QUIZBOT_TOKEN'))

dp = Dispatcher(storage=storage)
dp.include_router(router)

setup_dialogs(dp)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        dp.run_polling(bot)
    except KeyboardInterrupt:
        print('exit')