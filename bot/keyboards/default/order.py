from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from django.utils.translation import gettext as _

from bot.utils.category import get_all_category


async def get_order_type_keyboards() -> ReplyKeyboardMarkup:
    """
    Keyboard for choosing order type (take away or delivery).
    """
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="🏃‍♂️" + _(" Take away")),
                KeyboardButton(text="🚛 " + _("Delivery")),
            ],
            [
                KeyboardButton(text="⬅️ " + _("Back")),
            ]
        ]
    )

    return keyboard


async def get_takeaway_keyboards() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="⬅️ " + _("Back")),
            ],
            [
                KeyboardButton(text="📍 " + _("Determine nearest branch"), request_location=True),
            ],
            [
                KeyboardButton(text="🌐 " + _("Order here")),
                KeyboardButton(text=_("Select branch")),
            ]
        ]
    )

async def get_location_confirmation_keyboards() -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="⬅️ " + _("Back")), KeyboardButton(text="✅ " + _("Approve"))
            ],
            [
                KeyboardButton(text="📍 " + _("Send location")),
            ]
        ],
    )

async def get_menu_categories_keyboards() -> ReplyKeyboardMarkup:
    """
    Keyboard for choosing menu categories (2x2 grid layout).
    """
    return ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="⬅️ " + _("Back")),
                KeyboardButton(text="📥 " + _("Basket")),
            ],
            [
                KeyboardButton(text="🍱 " + _("Sets")),
                KeyboardButton(text="🍗 " + _("Chicken")),
            ],
            [
                KeyboardButton(text="🍟 " + _("Snacks")),
                KeyboardButton(text="🌯 " + _("Lesters")),
            ],
            [
                KeyboardButton(text="🍔 " + _("Burgers")),
                KeyboardButton(text="🌭 " + _("Longers/Hot-dog")),
            ],
            [
                KeyboardButton(text="🥤 " + _("Drinks")),
                KeyboardButton(text="🥗 " + _("Salads")),
            ],
            [
                KeyboardButton(text="🍩 " + _("Desserts")),
                KeyboardButton(text="👶 " + _("For kids")),
            ],
            [
                KeyboardButton(text="🍅 " + _("Sauces")),
            ],
        ]
    )


async def get_category_keyboard():
    products = await get_all_category()
    keyboards = ReplyKeyboardBuilder()
    if products:
        for product in products:
            keyboards.button(text=product.title)
        keyboards.button(text="⬅️ Back")
    else:
        keyboards.button(text="⬅️ Back")

    keyboards.adjust(2)
    return keyboards.as_markup(resize_keyboard=True)

async def get_order_by_keyboards() -> ReplyKeyboardMarkup:
    """
    Keyboard for choosing order type (take away or delivery).
    """
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(text="📥" + _(" Basket")),
            ],
            [
                KeyboardButton(text="⬅️ " + _("Back")),
            ]
        ]
    )

    return keyboard