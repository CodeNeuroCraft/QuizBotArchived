from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()

# База данных (в данном случае словарь)
registrations = {}

# класс регистрации
class Reg(StatesGroup):
    school = State()
    parallel = State()

@router.message(CommandStart())
async def send_welcome(message: Message) -> None:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text='Регистрация', callback_data='registration'),
                        InlineKeyboardButton(text='Другая кнопка', callback_data='other')]])
    await message.answer_photo(
        photo='https://vjoy.cc/wp-content/uploads/2019/07/13-1.jpg',
        caption="Текст под фото",
        reply_markup=keyboard)


@router.callback_query(F.data == 'registration')
async def process_registration(callback: CallbackQuery) -> None:
    await callback.answer()
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Да', callback_data='confirm_registration')]])
    await callback.message.answer('Вы уверены, что хотите зарегистрироваться?', reply_markup=keyboard)


@router.callback_query(F.data == 'confirm_registration')
async def confirm_registration(callback: CallbackQuery, state: FSMContext) -> None:
    await callback.answer()
    await callback.message.answer('Введите вашу школу:')
    registrations[callback.from_user.id] = {
        'school': None,
        'parallel': None,
    }
    await state.set_state(Reg.school)

@router.message(Reg.school)
async def process_school(message: Message, state: FSMContext) -> None:
    registrations[message.from_user.id]['school'] = message.text
    await message.answer('Введите вашу параллель:')
    await state.set_state(Reg.parallel)


@router.message(Reg.parallel)
async def process_parallel(message: Message) -> None:
    registrations[message.from_user.id]['parallel'] = message.text
    await message.answer('Вы успешно зарегистрированы!')