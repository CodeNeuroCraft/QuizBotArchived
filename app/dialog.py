from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram.filters.state import State, StatesGroup
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const

class MySG(StatesGroup):
    main = State()
    reg = State()
    hlp = State()


async def test(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.switch_to(MySG.hlp)

main_window = Window(
    Const('Добро пожаловать на викторину! Выберите пункт меню'),
    Button(Const('Регистрация'), id='reg'),
    Button(Const('Помощь'), id='hlp', on_click=test),
    state=MySG.main,
)

reg_window = Window(
    Const('Пока ничего тут нету. Но скоро появится)'),
    state=MySG.reg,
)

hlp_window = Window(
    Const('Пока ничего тут нету. Но скоро появится)'),
    state=MySG.hlp,
)

router = Router()
dialog = Dialog(main_window, reg_window, hlp_window)

@router.message(Command('start'))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MySG.main, mode=StartMode.RESET_STACK)