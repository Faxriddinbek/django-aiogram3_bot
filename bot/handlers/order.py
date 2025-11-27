from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from django.utils.translation import gettext as _

from bot.handlers.location import get_location_name
from bot.keyboards.default.order import get_takeaway_keyboards
from bot.states.order import OrderState

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
async def location_button_handler(message: Message, state: FSMContext):
    text = _("Please send your location using the button below")
    await message.answer(text=text)


@router.message(F.location, OrderState.location)
async def location_received_handler(message: Message, state: FSMContext):
    await state.update_data(
        longitude=message.location.longitude,
        latitude=message.location.latitude
    )
    await state.set_state(OrderState.category)

    data = await state.get_data()
    lat = data.get("latitude")
    lon = data.get("longitude")
    address = await get_location_name(latitude=lat, longitude=lon)
    text = _(f"Your address:{address}\n📍Confirm your location or resend it")
    await message.answer(text=text)