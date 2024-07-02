from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from aiogram_dialog import DialogManager, StartMode


from app.states.main_menu import MainMenu
from app.dialogs.main_menu.dialog import main_menu_dialog
from app.dialogs.reg.dialog import reg_dialog

linker = Router()
linker.include_router(main_menu_dialog)
linker.include_router(reg_dialog)

@linker.message(Command('start'))
async def start(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(MainMenu.main, mode=StartMode.RESET_STACK)