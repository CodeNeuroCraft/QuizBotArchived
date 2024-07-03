from aiogram.types import Message
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram.types import ContentType, CallbackQuery

from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo
from aiogram_dialog.widgets.text import Const
from aiogram_dialog.widgets.input import MessageInput
from aiogram_dialog import ShowMode


from app.states.reg import Reg
from . import on_event

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
                on_click=on_event.to_main
            ),
        ),
        state=Reg.confirm,
    ),
    Window(
        Const('Введите вашу школу:'),
        MessageInput(on_event.process_school, content_types=[ContentType.TEXT]),
        state=Reg.school,
    ),
    Window(
        Const('Введите вашу параллель:'),
        MessageInput(on_event.process_parallel, content_types=[ContentType.TEXT]),
        state=Reg.parallel,
    ),
    Window(
        Const('Вы успешно зарегистрированы!'),
        Button(
            Const('НАЗАД'),
            id='back',
            on_click=on_event.to_main
        ),
        state=Reg.success,
    ),
)