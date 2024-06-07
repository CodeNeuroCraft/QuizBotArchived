from aiogram import F, Router, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from . import reply_markups

router = Router()

# База данных (в данном случае словарь)
registrations = {}

class Reg(StatesGroup):
    school = State()
    parallel = State()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer_photo(
        photo='https://s320vla.storage.yandex.net/rdisk/92be87802f8936b828ab97e25d403c379491656c25f80032c38b0b3e9d0319d8/665e56f1/fKqInKw3d7bLFOeFnMGnhNMzEUTkKZr4jYPOrpJ05GlmkVc48paD3a7l7CB-t4XYiS6ARM97DXEHr0ViezbJTXqyxOH2stykHh8fxPqsluKr8npumZHI4midPdWhecNq?uid=0&filename=onwhite_hor%402x.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&fsize=11514&hid=40e4ca74811c38e28ee007d3da360f76&media_type=image&tknv=v2&etag=c35f367145c9db0611983cf5aecdb80f&ts=61a05021ede40&s=22c4653385c2a1c759efb2e44574217ba9fd29511b049ad0925bd81022f8b6bf&pb=U2FsdGVkX1994YtCz6aLB7sD5At1zBFuaM1_gFnGPAOFeC6om-U5EaXAhST3C1OVBeRUZHeJzGzjnrwskeZQi8WvNrfKGvDYouEjOVUYhQdeInmyrksvqp_T00cPvQK9',
        caption='Добро пожаловать на викторину! Выберите пункт меню',
        reply_markup=reply_markups.inline)



@router.callback_query(F.data == 'reg')
async def process_registration(callback: CallbackQuery, state: FSMContext):
    sent_msg = await callback.message.answer('Вы уверены, что хотите зарегистрироваться?', reply_markup=reply_markups.confirm)
    await state.update_data(last_msg_id=sent_msg.message_id)
    await callback.answer()


@router.callback_query(F.data == 'confirm_reg')
async def confirm_registration(callback: CallbackQuery, bot: Bot, state: FSMContext):
    sent_msg = await bot.edit_message_text('Введите вашу школу:', callback.message.chat.id, (await state.get_data())['last_msg_id'], reply_markup=None)
    registrations[callback.from_user.id] = {
        'school': None,
        'parallel': None,
    }
    await state.set_state(Reg.school)
    await state.update_data(last_msg_id=sent_msg.message_id)
    await callback.answer()


@router.message(Reg.school)
async def process_school(message: Message, bot: Bot, state: FSMContext):
    registrations[message.from_user.id]['school'] = message.text
    await message.delete()
    sent_msg = await bot.edit_message_text('введите вашу параллель:', message.chat.id, (await state.get_data())['last_msg_id'])
    await state.set_state(Reg.parallel)
    await state.update_data(last_msg_id=sent_msg.message_id)


@router.message(Reg.parallel)
async def process_parallel(message: Message, bot: Bot, state: FSMContext):
    registrations[message.from_user.id]['parallel'] = message.text
    await message.delete()
    await bot.edit_message_text('Вы успешно зарегистрированы!', message.chat.id, (await state.get_data())['last_msg_id'])
    
    
# @router.callback_query(F.data == 'decline_reg')
# async def decline_registration(callback: CallbackQuery, state: FSMContext):
#     await state.set_state(Reg.start)
#     await callback.answer()