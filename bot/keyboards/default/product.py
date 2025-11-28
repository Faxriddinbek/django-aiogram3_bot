from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.utils.product import get_sets_products, get_snacks_products, get_burgerlar_products, get_tovuq_products, \
    get_lesterlar_products, get_hot_dog_products


async def get_product_sets_keyboard():
    products = await get_sets_products()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)


async def get_product_snacks_keyboard():
    products = await get_snacks_products()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)


async def get_product_burgerlar_keyboard():
    products = await get_burgerlar_products()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)


async def get_product_tovuq_keyboard():
    products = await get_tovuq_products()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)


async def get_product_lesterlar_keyboard():
    products = await get_lesterlar_products()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)


async def get_product_hot_dog_keyboard():
    products = await get_hot_dog_products()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)