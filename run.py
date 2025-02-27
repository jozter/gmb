from aiogram import Bot, Dispatcher
from app.hendlers import router
from aiogram.types import BotCommand
from dotenv import load_dotenv
import os

load_dotenv()

bot = os.getenv("TOKEN")
dp = Dispatcher()

async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/start',
                   description='Запуск бота')]
    await bot.set_my_commands(main_menu_commands)

if __name__ == '__main__':
    dp.startup.register(set_main_menu)
    dp.include_router(router)
    dp.run_polling(bot, none_stop=True)
    
