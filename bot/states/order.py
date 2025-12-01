from aiogram.fsm.state import StatesGroup, State


class OrderState(StatesGroup):
    order_type = State()
    location = State()
    category = State()
    product_category = State()
    location_select = State()
    order_by = State()