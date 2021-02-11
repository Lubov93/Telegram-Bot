from aiogram.dispatcher.filters import Command
import logging
from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, remont_keyboard, stroys_keyboard
from loader import dp, bot
from aiogram.types import Message, CallbackQuery







@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text="На продажу у нас есть 2 услуги: Ремонтные и строительные работы. \n"
                              "Если вам ничего не нужно - жмите отмену",
                         reply_markup=choice)


@dp.callback_query_handler(text_contains="remont")
async def buying_remont(call: CallbackQuery):
    # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
    # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
    await call.answer(cache_time=60)

    callback_data = call.data

    # Отобразим что у нас лежит в callback_data
    # logging.info(f"callback_data='{callback_data}'")
    # В Python 3.8 можно так, если у вас ошибка, то сделайте предыдущим способом!
    logging.info(f"{callback_data=}")

    await call.message.answer("Вы выбрали услуги ремонта.Спасибо.",
                              reply_markup=remont_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name="stroys"))
async def buying_stroys(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)
    logging.info(f"{callback_data=}")
    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали услуги строительства. Услуги строительства наличивают всего {quantity} услуг. Спасибо.",
                              reply_markup=stroys_keyboard)