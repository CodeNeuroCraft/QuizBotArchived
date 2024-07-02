from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.media import StaticMedia
from aiogram.types import ContentType
from aiogram_dialog.widgets.kbd import Row, SwitchTo, Start
from aiogram_dialog.widgets.text import Const

from app.states.main_menu import MainMenu
from app.states.reg import Reg

main_menu_dialog = Dialog(
    Window(
        StaticMedia(
            url='https://downloader.disk.yandex.ru/preview/a2db807363a125c36e093c96d62c51fbc6285868179286ba3e670c83f2ee2b2f/667b2587/R62WU8dtk7-Q0djji7n-cmxE-rn890DjbBvDmq6ghcaYktDbn6tkZFArOExvqcvTbhQWrZ6Z6FOTcyT3jT8zNQ%3D%3D?uid=0&filename=onwhite_ver.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=1920x918',
            type=ContentType.PHOTO
        ),
        Const('Добро пожаловать на викторину! Выберите пункт меню'),
        Row(
            Start(
                Const('Регистрация'),
                id='reg',
                state=Reg.confirm
            ),
            SwitchTo(
                Const('Помощь'),
                id='help',
                state=MainMenu.help
            ),
        ),
        state=MainMenu.main,
    ),
    Window(
        Const('Пока ничего тут нету. Но скоро появится)'),
        SwitchTo(
            Const('НАЗАД'),
            id='back',
            state=MainMenu.main
        ),
        state=MainMenu.help,
    ),
)