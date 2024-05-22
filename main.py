import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
import aiogram.types

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("TOKEN")

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()
bot = Bot(token=TOKEN)

# База данных (в данном случае словарь)
registrations = {}


@dp.message(CommandStart())
async def send_welcome(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Регистрация', callback_data='registration'),
                        InlineKeyboardButton(text='Другая кнопка', callback_data='other')]])
    await message.answer_photo(
        photo='https://vjoy.cc/wp-content/uploads/2019/07/13-1.jpg',
        caption="Текст под фото",
        reply_markup=keyboard)


@dp.callback_query(F.data == 'registration')
async def process_registration(callback: CallbackQuery):
    await callback.answer()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да', callback_data='confirm_registration')]])
    await callback.message.answer('Вы уверены, что хотите зарегистрироваться?', reply_markup=keyboard)


@dp.callback_query_handler(F.data == 'confirm_registration')
async def confirm_registration(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer('Введите вашу школу:')
    registrations[callback.from_user.id] = {
        'school': None,
        'parallel': None,
    }
    await bot.register_next_step_handler(callback.message, process_school)


async def process_school(message: Message):
    registrations[message.from_user.id]['school'] = message.text
    await message.answer('Введите вашу параллель:')
    await bot.register_next_step_handler(message, process_parallel)


async def process_parallel(message: Message):
    registrations[message.from_user.id]['parallel'] = message.text
    await message.answer('Вы успешно зарегистрированы!')


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except KeyboardInterrupt:
        print('exit')