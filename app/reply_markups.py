from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='регистрация',callback_data='reg'),
    InlineKeyboardButton(text='помощь', callback_data='help')
    ]])

confirm = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Да', callback_data='confirm_reg'),
    InlineKeyboardButton(text='Нет', callback_data='decline_reg')
    ]])