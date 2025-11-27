from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.utils.product import get_all_products


async def get_cities_keyboard():
    products = await get_all_products()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)