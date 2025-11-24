from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):# bu quyidagi steatelarga tushuradi
    language = State()
    location = State()
    menu = State()
    order = State()
    order_story = State()
    settings = State()
    team = State()
    about = State()
    action = State()
    phone_number = State()