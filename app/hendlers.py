from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.enums import ParseMode
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import app.keyboards as kb
from app.lexicon import lexicone as lx
from dotenv import load_dotenv
import os

load_dotenv()

router=Router()
TOKEN = os.getenv("TOKEN")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")
bot = Bot(token=TOKEN)

message_ids = {}
# Создаём состояния
class PhotoState(StatesGroup):
    waiting_for_photo = State()
    waiting_for_caption = State()

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

# Обрабатываем кнопку "Контейнер заполнен"
@router.message(F.text == "Контейнер заполнен")
async def container_filled(message: Message, state: FSMContext):
    await message.answer("Супер! Отправь фотографию контейнера, пожалуйста.")
    await state.set_state(PhotoState.waiting_for_photo)

# Игнорируем фото, если бот не ждет их
@router.message(F.photo)
async def ignore_unexpected_photo(message: Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state == PhotoState.waiting_for_photo.state:
        await process_photo(message, state)

# Обрабатываем фото от пользователя
async def process_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id, user=message.from_user)

    # Инлайн-кнопка "Пропустить"
    skip_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Пропустить", callback_data="skip_caption")]
        ]
    )

    await message.answer("Ты можешь указать контейнер, оставить коммменатрий или нажать 'Пропустить' ⭐️.", reply_markup=skip_button)
    await state.set_state(PhotoState.waiting_for_caption)

# Обрабатываем текстовое сообщение (если пользователь сам вводит текст)
@router.message(PhotoState.waiting_for_caption, F.text)
async def process_caption(message: Message, state: FSMContext):
    data = await state.get_data()
    photo_id = data['photo']
    user = data['user']

    # Формируем информацию об отправителе
    user_info = f"▪️ *Отправитель:*\n"
    user_info += f"▫️ ID: `{user.id}`\n"
    if user.username:
        user_info += f"▫️ @{user.username}\n"
    if user.full_name:
        user_info += f"▫️ Имя: {user.full_name}\n"

    caption = f"^.^ Информация по контейнеру\n💬 {message.text}\n\n{user_info}"

    # Отправляем фото и текст в нужный чат
    await message.bot.send_photo(ADMIN_CHAT_ID, photo=photo_id, caption=caption, parse_mode="Markdown")

    await message.answer("Спасибо тебе за участие! 🩵 ")
    await state.clear()  # Завершаем состояние

# Обрабатываем нажатие кнопки "Пропустить"
@router.callback_query(F.data == "skip_caption")
async def skip_caption(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    photo_id = data['photo']
    user = data['user']

    # Формируем информацию об отправителе
    user_info = f"▪️ *Отправитель:*\n"
    user_info += f"▫️ ID: `{user.id}`\n"
    if user.username:
        user_info += f"▫️ @{user.username}\n"
    if user.full_name:
        user_info += f"▫️ Имя: {user.full_name}\n"

    caption = f"^.^ Информация по контейнеру\n💬 Без комментариев\n\n{user_info}"

    # Отправляем фото без подписи
    await callback_query.message.bot.send_photo(ADMIN_CHAT_ID, photo=photo_id, caption=caption, parse_mode="Markdown")

    await callback_query.message.answer("Спасибо тебе за участие! 🩵 ")
    await callback_query.answer()  # Закрываем уведомление
    await state.clear()  # Завершаем состояние
    
###################     АЙДИ ЧАТА     ########################################################### 

@router.message(Command("chat_id"))
async def cmd_chat_id(message: Message):
    await message.answer(f"ID этого чата: {message.chat.id}")

###################     АЙДИ ТРЕДА     ########################################################### 

@router.message(F.text == "Please, скажи мне id этой темы")
async def get_thread_id(message: Message):
    if message.message_thread_id:
        await message.reply(f"ID этой темы: {message.message_thread_id}")
    else:
        await message.reply("Это сообщение не в теме, здесь нет ID.")