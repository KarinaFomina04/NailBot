import os
import asyncio

from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
import create_database as db_creator
from models.database import DATABASE_NAME

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    from handlers import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)



