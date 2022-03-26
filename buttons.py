from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from callback import open_menu_callback

price_and_record = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Прайс и запись",
            callback_data=open_menu_callback.new(menu="price_and_record", id="0")
        )
    ]
])



complexes = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text="Комплекс маникюр",
            callback_data=open_menu_callback.new(menu="complex_manicure", id="0")
        )
    ],
    [
        InlineKeyboardButton(
            text="Комплекс наращивания",
            callback_data=open_menu_callback.new(menu="nail_extension", id="0")
        )
    ]

])
