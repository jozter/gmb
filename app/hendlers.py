from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
import app.keyboards as kb
from app.lexicon import lexicone as lx
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router=Router()

resp_id = None 
resp_id1 = None

@router.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer(text=lx['/start'], parse_mode=ParseMode.HTML, reply_markup=kb.menu)
    
####################################КНОПКА СОРТИРОВКА###############################################

@router.message(F.text=='Сортировка в МИСИС')
async def inline_sort(message: Message):
    global resp_id
    await message.answer(text='Раздельный сбор отходов', reply_markup=kb.set_sort) 
    resp_message = await message.answer(text='Выбери место.')
    resp_id = resp_message.message_id

@router.callback_query(lambda c: c.data.startswith('sort'))
async def sortirovka(callback: CallbackQuery):
    global resp_id
    await callback.answer()
    response_text = lx.get(callback.data, "Неизвестный вариант")
    if resp_id:
        try:
            await callback.bot.edit_message_text(
                text=response_text,
                chat_id=callback.message.chat.id,
                message_id=resp_id,
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            print(f"Error editing message: {e}")
    else:
        sent_message = await callback.message.answer(response_text)
        resp_id = sent_message.message_id
       
#################################НЕРАБОЧЕЕЕ########################################################## 

@router.message(F.text=='Контейнер заполнен')
async def start(message: Message):
    await message.answer(text="Функция на доработке, скоро мы ее добавим. 💚")
    
@router.message(F.text=='Есть вопрос')
async def start(message: Message):
    await message.answer(text="Функция на доработке, скоро мы ее добавим. 💚")
    
###############################КНОПКА О НАС##############################################
    
@router.message(F.text=='О нас')
async def inline_sort(message: Message):
    global resp_id1
    await message.answer(lx.get('1about1'), reply_markup=kb.set_about, parse_mode=ParseMode.HTML) 
    resp_message1 = await message.answer(text='Выбери, что хочешь узнать.')
    resp_id1 = resp_message1.message_id

@router.callback_query(lambda c: c.data.startswith('about'))
async def sortirovka(callback: CallbackQuery):
    global resp_id1
    await callback.answer()
    response_text = lx.get(callback.data, "Неизвестный вариант")
    if resp_id1:
        try:
            await callback.bot.edit_message_text(
                text=response_text,
                chat_id=callback.message.chat.id,
                message_id=resp_id1,
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            print(f"Error editing message: {e}")
    else:
        sent_message1 = await callback.message.answer(response_text)
        resp_id1 = sent_message1.message_id

###############################КНОПКА УЗНАТЬ О СОТРИРОВКЕ##############################################

@router.message(F.text=='Подготовка вторсырья')
async def start(message: Message):
    await message.answer(lx.get('prepearing_waste'), parse_mode=ParseMode.HTML)


