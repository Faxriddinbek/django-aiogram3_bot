from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from django.utils.translation import gettext as _

from bot.keyboards.default.order import get_order_type_keyboards, get_takeaway_keyboards, get_category_keyboard
from bot.keyboards.default.user import get_user_main_keyboards
from bot.states.order import OrderState

router = Router()


@router.message(F.text.in_(['⬅️ Back', '⬅️ Ortga']), OrderState.order_type)
async def make_order_handler(message: Message, state: FSMContext):
    text = _('Welcome to main menu 😊')
    await message.answer(text=text, reply_markup=await get_user_main_keyboards())
    await state.clear()


@router.message(F.text.in_(['⬅️ Back', '⬅️ Ortga']), OrderState.location)
async def make_order_handler(message: Message, state: FSMContext):
    await state.set_state(OrderState.order_type)

    text = _("Take away  🙋‍♂️ or delivery 🚙")
    await message.answer(text=text, reply_markup=await get_order_type_keyboards())

@router.message(F.text.in_(['⬅️ Back', '⬅️ Ortga']), OrderState.location_select)
async def make_order_handler(message: Message, state: FSMContext):
    await state.set_state(OrderState.location)

    text = _("Take away  🙋‍♂️ or delivery 🚙")
    await message.answer(text=text, reply_markup=await get_takeaway_keyboards())

@router.message(F.text.in_(['⬅️ Back', '⬅️ Ortga']), OrderState.category)
async def make_order_handler(message: Message, state: FSMContext):
    await state.set_state(OrderState.location)

    text = _("Take away  🙋‍♂️ or delivery 🚙")
    await message.answer(text=text, reply_markup=await get_takeaway_keyboards())


@router.message(F.text.in_(['⬅️ Back', '⬅️ Ortga']), OrderState.location_select)
async def make_order_handler(message: Message, state: FSMContext):
    await state.set_state(OrderState.category)

    text = _("Where to start?")
    await message.answer(text=text, reply_markup=await get_category_keyboard())