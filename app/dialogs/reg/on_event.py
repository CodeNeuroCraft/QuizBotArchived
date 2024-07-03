from aiogram.types import Message
from aiogram_dialog import DialogManager
from aiogram.types import CallbackQuery

from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode


from app.states.reg import Reg

async def to_main(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.done()

# База данных (в данном случае словарь)
registrations = {}

async def process_school(
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

async def process_parallel(
        message: Message,
        message_input: MessageInput,
        manager: DialogManager,
):
    manager.show_mode=ShowMode.EDIT
    registrations[message.from_user.id]['parallel'] = message.text
    await message.delete()
    await manager.switch_to(Reg.success)