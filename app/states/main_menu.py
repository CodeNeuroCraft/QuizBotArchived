from aiogram.filters.state import State, StatesGroup

class MainMenu(StatesGroup):
    main = State()
    hlp = State()