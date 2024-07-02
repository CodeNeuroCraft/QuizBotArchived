from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram.types import ContentType, CallbackQuery

from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode


from app.states.reg import Reg

# База данных (в данном случае словарь)
registrations = {}

async def to_main(callback: CallbackQuery, button: Button, manager: DialogManager):
    await manager.done()

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

reg_dialog = Dialog(
    Window(
        Const('Вы уверены, что хотите зарегистрироваться?'),
        Row(
            SwitchTo(
                Const('ДА'),
                id='school',
                state=Reg.school
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