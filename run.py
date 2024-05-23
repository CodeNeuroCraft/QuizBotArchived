import asyncio
import logging
import sys

from dotenv import load_dotenv
from os import getenv
load_dotenv()

from app.handlers import router

from aiogram import Bot, Dispatcher

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(token=getenv('TOKEN'))


async def main() -> None:
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')