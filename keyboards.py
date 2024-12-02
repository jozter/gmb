from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)


menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Сортировка в МИСИС'), KeyboardButton(text='Контейнер заполнен')],
    [KeyboardButton(text='Подготовка вторсырья'), KeyboardButton(text='О нас')],
    [KeyboardButton(text='Есть вопрос')]
    ],
                           resize_keyboard=True)

    
set_sort = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Точка кипения Комунна', callback_data='sort1')],
    [InlineKeyboardButton(text='Корпус Б', callback_data='sort2')],
    [InlineKeyboardButton(text='Горняк-1', callback_data='sort3')],
    [InlineKeyboardButton(text='Металлург-3', callback_data='sort4')],
    [InlineKeyboardButton(text='Медиацентр', callback_data='sort5')],
    [InlineKeyboardButton(text='СтудОфис', callback_data='sort6')]
    ])

set_full = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Точка кипения Комунна', callback_data='full1')],
    [InlineKeyboardButton(text='Корпус Б', callback_data='full2')],
    [InlineKeyboardButton(text='Горняк-1', callback_data='full3')],
    [InlineKeyboardButton(text='Металлург-3', callback_data='full4')],
    [InlineKeyboardButton(text='Медиацентр', callback_data='full5')],
    [InlineKeyboardButton(text='СтудОфис', callback_data='full6')],
    ])

set_about = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Наши проекты', callback_data='about1')],
    [InlineKeyboardButton(text='Социальные сети', callback_data='about2')],
    [InlineKeyboardButton(text='Вступить в клуб', callback_data='about3')],
    ])

set_full_data = {
    'full1': ['Стекло', 'Пластиковые бутылки', 'Макулатура', 'Батарейки', 'Крышки от бутылок', 'Пластиковые стаканчики'],
    'full2': ['Крышки от бутылок', 'Электронки'],
    'full3': ['Крышки от бутылок', 'Батарейки'],
    'full4': ['Крышки от бутылок'],
    'full5': ['Пластиковые стаканчики', 'Электронки', 'Батарейки'],
    'full6': ['Чеки', 'Блистеры']
}

def generate_full_keyboard(callback_data: str):
    keyboard = InlineKeyboardMarkup()
    for item in set_full_data.get(callback_data, []):
        keyboard.add(InlineKeyboardButton(text=item, callback_data=f"{callback_data}_{item.lower().replace(' ', '_')}"))
    return keyboard