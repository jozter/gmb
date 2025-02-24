from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.enums import ParseMode
import app.keyboards as kb
from app.lexicon import lexicone as lx
from config import TOKEN

router=Router()
bot = Bot(token=TOKEN)

message_ids = {}

@router.message(Command(commands=["start"]))
async def start(message: Message):
    await message.answer(text=lx['/start'], parse_mode=ParseMode.HTML, reply_markup=kb.menu)
    
###################     КНОПКА СОРТИРОВКА     ###############################################

@router.message(F.text=='Сортировка в МИСИС')
async def inline_sort(message: Message):
    chat_id = message.chat.id
    await message.answer(text='Что ты хочешь сдать?', reply_markup=kb.set_sort) 
    resp_message = await message.answer(text='Выбери фракцию.')
    message_ids[chat_id] = resp_message.message_id

@router.callback_query(lambda c: c.data.startswith('sort'))
async def sortirovka(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    await callback.answer()
    response_text = lx.get(callback.data, "Неизвестный вариант")
    
    if chat_id in message_ids:
        try:
            await callback.bot.edit_message_text(
                text=response_text,
                chat_id=chat_id,
                message_id=message_ids[chat_id],
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
           print(f"Error editing message: {e}")
    else:
        sent_message = await callback.message.answer(response_text)
        message_ids[chat_id] = sent_message.message_id
###################     КНОПКА ЕСТЬ ВОПРОС     #############################################    

@router.message(F.text=='Есть вопрос')
async def start(message: Message):
    await message.answer(text="Если у тебя есть вопрос или предложение - пиши @twwdy. 🧚‍♀️")

###################     КНОПКА О НАС     #######################################    

@router.message(F.text == 'О нас')
async def inline_sort(message: Message):
    chat_id = message.chat.id
    await message.answer(lx.get('1about1'), reply_markup=kb.set_about, parse_mode=ParseMode.HTML)
    resp_message1 = await message.answer(text='Выбери, что хочешь узнать.')
    message_ids[chat_id] = resp_message1.message_id  

@router.callback_query(lambda c: c.data.startswith('about'))
async def sortirovka(callback: CallbackQuery):
    chat_id = callback.message.chat.id
    await callback.answer()
    response_text = lx.get(callback.data, "Неизвестный вариант")

    if chat_id in message_ids:
        try:
            await callback.bot.edit_message_text(
                text=response_text,
                chat_id=chat_id,
                message_id=message_ids[chat_id],
                parse_mode=ParseMode.HTML
            )
        except Exception as e:
            print(f"Error editing message: {e}")
    else:
        sent_message1 = await callback.message.answer(response_text)
        message_ids[chat_id] = sent_message1.message_id
        
###################     КНОПКА УЗНАТЬ О СОТРИРОВКЕ     ########################################

@router.message(F.text=='Подготовка вторсырья')
async def start(message: Message):
    await message.answer(lx.get('prepearing_waste'), parse_mode=ParseMode.HTML)

###################     КНОПКА КОНТЕЙНЕР ЗАПОЛНЕН     ##################################################### 

@router.message(F.text == "Контейнер заполнен")
async def container_filled(message: Message):
    #await message.answer("Отправь фотографию контейнера, пожалуйста, а так же можешь добавить текст:")
    await message.answer("Работаем над этой функцией ^.^")

###################     АЙДИ ЧАТА     ########################################################### 

@router.message(Command("chat_id"))
async def cmd_chat_id(message: Message):
    await message.answer(f"ID этого чата: {message.chat.id}")

