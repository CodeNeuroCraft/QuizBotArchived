from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram.types import ContentType
from aiogram_dialog.widgets.kbd import Button, Row
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode

from .states.main_menu import MainMenu
from .states.reg import Reg

# База данных (в данном случае словарь)
registrations = {}

# getters

async def help(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(MainMenu.hlp)

async def to_main(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(MainMenu.main)

async def to_reg(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.start(Reg.confirm)

async def confirm_reg(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(Reg.confirm)

async def ask_school(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(Reg.school)

async def ask_parallel(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(Reg.parallel)

async def school_handler(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode=ShowMode.EDIT
    registrations[message.from_user.id] = {
        'school': None,
        'parallel': None,
    }
    registrations[message.from_user.id]['school'] = message.text
    await message.delete()
    await manager.switch_to(Reg.parallel)

async def parallel_handler(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode=ShowMode.EDIT
    registrations[message.from_user.id]['parallel'] = message.text
    await message.delete()
    await manager.switch_to(Reg.success)

first = Dialog(
    Window(
        StaticMedia(
            url='https://downloader.disk.yandex.ru/preview/a2db807363a125c36e093c96d62c51fbc6285868179286ba3e670c83f2ee2b2f/667b2587/R62WU8dtk7-Q0djji7n-cmxE-rn890DjbBvDmq6ghcaYktDbn6tkZFArOExvqcvTbhQWrZ6Z6FOTcyT3jT8zNQ%3D%3D?uid=0&filename=onwhite_ver.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x918',
            type=ContentType.PHOTO
        ),
        Const('Добро пожаловать на викторину! Выберите пункт меню'),
        Row(
            Button(
                Const('Регистрация'),
                id='reg',
                on_click=to_reg
            ),
            Button(
                Const('Помощь'),
                id='hlp',
                on_click=help
            ),
        ),
        state=MainMenu.main,
    ),
    Window(
        Const('Пока ничего тут нету. Но скоро появится)'),
        Button(
            Const('НАЗАД'),
            id='back',
            on_click=to_main
        ),
        state=MainMenu.hlp,
    ),
)

second = Dialog(
    Window(
        Const('Вы уверены, что хотите зарегистрироваться?'),
        Row(
            Button(
                Const('ДА'),
                id='school',
                on_click=ask_school
            ),
            Button(
                Const('НЕТ'),
                id='back',
                on_click=to_main
            ),
        ),
        state=Reg.confirm,
    ),
    Window(
        Const('Введите вашу школу:'),
        MessageInput(school_handler, content_types=[ContentType.TEXT]),
        state=Reg.school,
    ),
    Window(
        Const('Введите вашу параллель:'),
        MessageInput(parallel_handler, content_types=[ContentType.TEXT]),
        state=Reg.parallel,
    ),
    Window(
        Const('Вы успешно зарегистрированы!'),
        Button(
            Const('НАЗАД'),
            id='back',
            on_click=to_main
        ),
        state=Reg.success,
    ),
)

router = Router()

@router.message(Command('start'))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main, mode=StartMode.RESET_STACK)