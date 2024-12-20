from aiogram.fsm.state import StatesGroup, State

class get_voice(StatesGroup):
    audio = State()

class delete_voice(StatesGroup):
    id = State()
    confirm = State()

class BotTarif:
    def __init__(self, name, quantity, id):
        self.name = name
        self.quantity = quantity
        self.id = id