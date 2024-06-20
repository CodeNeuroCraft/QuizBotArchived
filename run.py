import asyncio
import logging
import sys

from os import getenv

from app.handlers import router

from aiogram import Bot, Dispatcher



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