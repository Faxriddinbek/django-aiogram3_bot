from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from django.utils.translation import gettext as _

from bot.handlers.location import get_location_name
from bot.keyboards.default.order import get_takeaway_keyboards, get_location_confirmation_keyboards, \
    get_menu_categories_keyboards, get_category_keyboard, get_order_by_keyboards
from bot.keyboards.default.product import get_product_sets_keyboard, get_product_snacks_keyboard, \
    get_product_burgerlar_keyboard, get_product_tovuq_keyboard, get_product_lesterlar_keyboard, \
    get_product_hot_dog_keyboard
from bot.models.product import Product
from bot.states.order import OrderState
from bot.utils.product import get_sets_products, get_product_by_title

router = Router()


@router.message(F.text.in_(['🏃‍♂️ Take away', '🏃‍♂️ Olib kelish']), OrderState.order_type)
async def take_away_handler(message: Message, state: FSMContext):
    await state.update_data(order_type='take_away')
    await state.set_state(OrderState.location)

    text = _("Where are you? Send your location and we determine the nearest branch to you")
    await message.answer(text=text, reply_markup=await get_takeaway_keyboards())


@router.message(
    F.text.in_(['📍 Determine nearest branch', '📍 Manzilni ulashish']),
    OrderState.location
)
async def location_handler(message: Message, state: FSMContext):
    text = _("Please send your location using the button below")
    await message.answer(text=text)


@router.message(F.location, OrderState.location)
async def location_button_handler(message: Message, state: FSMContext):
    await state.update_data(
        longitude=message.location.longitude,
        latitude=message.location.latitude
    )
    data = await state.get_data()
    lat = data.get("latitude")
    lon = data.get("longitude")
    address = await get_location_name(latitude=lat, longitude=lon)
    text = _(f"Your address:{address}\n📍Confirm your location or resend it")
    await message.answer(text=text, reply_markup=await get_location_confirmation_keyboards())
    await state.set_state(OrderState.location_select)


@router.message(F.text.in_(['✅ Approve', '✅ Tasdiqlash']), OrderState.location_select)
async def location_received_handler(message: Message, state: FSMContext):
    text = _("Where to start?")
    await message.answer(text=text, reply_markup=await get_category_keyboard())
    await state.set_state(OrderState.category)


@router.message(F.text, OrderState.category)
async def category_handler(message: Message, state: FSMContext):
    data = message.text
    text = _("Where to start?")
    if data == "🍱 Setlar":
        await message.answer(text=text, reply_markup=await get_product_sets_keyboard())
    elif data == "🍟 Sneklar":
        await message.answer(text=text, reply_markup=await get_product_snacks_keyboard())
    elif data == "🍔 Burgerlar":
        await message.answer(text=text, reply_markup=await get_product_burgerlar_keyboard())
    elif data == "🍗 Tovuq":
        await message.answer(text=text, reply_markup=await get_product_tovuq_keyboard())
    elif data == "🌯 Lesterlar":
        await message.answer(text=text, reply_markup=await get_product_lesterlar_keyboard())
    elif data == "🌭 Longerlar/Hot-dog":
        await message.answer(text=text, reply_markup=await get_product_hot_dog_keyboard())
    await state.set_state(OrderState.product_category)


@router.message(F.text, OrderState.product_category)
async def product_category_handler(message: Message, state: FSMContext):
    messages = message.text
    data = await get_product_by_title(messages)
    await message.answer(text=data, reply_markup=await get_order_by_keyboards())
    await state.set_state(OrderState.order_by)


@router.message(F.text.in_(['📥 Add to the basket ✅', "📥 Savatga qo'shish ✅"]), OrderState.product_category)
async def product_category_handler(message: Message, state: FSMContext):
    messages = message.text
    if messages == "📥 Add to the basket ✅" or "📥 Savatga qo'shish ✅":
        data = Product.objects.get("Mahsulot savatga muvaffaqiyatli qo'shildi ✅")
    elif messages == "⬅️ Ortga":
        data = Product.objects.get("Nimadan boshlaymiz?")
    await message.answer(text=data, reply_markup=await get_category_keyboard())
    await state.set_state(OrderState.category)

# @router.message(F.location, OrderState.location_select)
# async def location_select_handler(message: Message, state: FSMContext):
#     await state.update_data(
#         longitude=message.location.longitude,
#         latitude=message.location.latitude
#     )
#     text = _("Where to start?")
#     await message.answer(text=text, reply_markup= await get_menu_categories_keyboards())
#     await state.set_state(OrderState.category)
