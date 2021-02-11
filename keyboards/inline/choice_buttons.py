from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import URL_STROYS, URL_REMONTS
from keyboards.inline.callback_datas import buy_callback



# Вариант 2 - с помощью row_width и insert.
choice = InlineKeyboardMarkup(row_width=2)

buy_remont = InlineKeyboardButton(text="Купить услуги ремонта", callback_data=buy_callback.new(item_name="remont", quantity=1))
choice.insert(buy_remont)

buy_stroys = InlineKeyboardButton(text="Купить услуги строительства", callback_data="buy:stroys:5")
choice.insert(buy_stroys)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)


# А теперь клавиатуры со ссылками на товары
remont_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_REMONTS)
    ]
])

stroys_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url=URL_STROYS)
    ]
])