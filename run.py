from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from os import getenv
import logging, sys

from app.dialog import dialog, router


storage = MemoryStorage()
bot = Bot(token=getenv('TOKEN'))
dp = Dispatcher(storage=storage)
dp.include_router(dialog)
dp.include_router(router)
setup_dialogs(dp)


if __name__ == '__main__':
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        dp.run_polling(bot)
    except KeyboardInterrupt:
        print('exit')