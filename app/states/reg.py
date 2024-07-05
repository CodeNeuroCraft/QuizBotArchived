from aiogram.filters.state import State, StatesGroup

class Reg(StatesGroup):
    confirm = State()
    school = State()
    parallel = State()
    check = State()
    success = State()