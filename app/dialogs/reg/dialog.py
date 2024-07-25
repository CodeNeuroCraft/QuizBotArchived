from aiogram_dialog import Dialog, Window
from aiogram.types import ContentType

from aiogram_dialog.widgets.kbd import Button, Row, SwitchTo
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.input import MessageInput


from app.states.reg import Reg
from . import on_event



reg_dialog = Dialog(
    Window(
        Const('Вы уверены, что хотите зарегистрироваться?'),
        Row(
            SwitchTo(
                Const('ДА'),
                id='school',
                state=Reg.school,
                on_click=on_event.start_reg,
            ),
            Button(
                Const('НЕТ'),
                id='back',
                on_click=on_event.to_main,
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
        Const('Введенные данные:'),
        Format('Школа: {school};'),
        Format('Параллель: {parallel};'),
        Row(
            SwitchTo(
                Const('ВСЁ ВЕРНО'),
                id='success',
                state=Reg.success,
                on_click=on_event.end_reg
            ),
            SwitchTo(
                Const('ХРЕНЬ'),
                id='confirm',
                state=Reg.confirm,
                on_click=on_event.abort_reg
            ),
        ),
        getter=on_event.registrations.get_session_data,
        state=Reg.check,
    ),
    Window(
        Const('Вы успешно зарегистрированы!'),
        Button(
            Const('НАЗАД'),
            id='back',
            on_click=on_event.to_main,
        ),
        state=Reg.success,
    ),
)