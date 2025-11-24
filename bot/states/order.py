from aiogram.fsm.state import State, StatesGroup

class Order(StatesGroup):
    Orders = State()
    Order_location = State()
    Order_yetkazish = State()
    Order_story = State()
    Order_register = State()