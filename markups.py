from aiogram import types
markup_subscribe = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='ПОДПИСАЛСЯ', callback_data='sub')]])
admin_panel = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='Список звуков', callback_data='list_voice')],[types.InlineKeyboardButton(text='Добавить', callback_data='add_voice'), types.InlineKeyboardButton(text='Удалить', callback_data='delete_voice')], [types.InlineKeyboardButton(text='Личный Кабинет', callback_data='cabinet')]])
cancel = types.InlineKeyboardMarkup(inline_keyboard=[[types.InlineKeyboardButton(text='отмена', callback_data='cancel')]])