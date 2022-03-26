from aiogram import types
from aiogram.dispatcher.filters import CommandStart
from aiogram.types import CallbackQuery

from buttons import price_and_record
from callback import open_menu_callback
from main import bot, dp
from config import ADMINS


async def send_to_admin(dp):
    for admin in ADMINS:
        await dp.bot.send_message(admin, "Бот Запущен")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Добро пожаловать, {message.from_user.full_name}!\nМеню:", reply_markup=price_and_record)


@dp.callback_query_handler(open_menu_callback.filter(menu="price_and_record"))
async def open_price_and_record(call: CallbackQuery):
    await call.message.edit_text("Прайс и запись")
