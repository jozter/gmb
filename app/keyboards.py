from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Сортировка в МИСИС'), KeyboardButton(text='Контейнер заполнен')],
    [KeyboardButton(text='Подготовка вторсырья'), KeyboardButton(text='О нас')],
    [KeyboardButton(text='Есть вопрос')]
    ],
                           resize_keyboard=True)

    
set_sort = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Крышечки от бутылок', callback_data='sort1')],
    [InlineKeyboardButton(text='Батарейки', callback_data='sort2')],
    [InlineKeyboardButton(text='Электронные сигареты', callback_data='sort3')],
    [InlineKeyboardButton(text='Блистеры от лекарств', callback_data='sort4')],
    [InlineKeyboardButton(text='Чеки', callback_data='sort5')],
    [InlineKeyboardButton(text='Пластиковые стаканчики', callback_data='sort6')]
    ])

set_about = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Наши проекты', callback_data='about1')],
    [InlineKeyboardButton(text='Социальные сети', callback_data='about2')],
    [InlineKeyboardButton(text='Вступить в клуб', callback_data='about3')],
    ])