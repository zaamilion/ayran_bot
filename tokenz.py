import json
from functions import dict_to_class
from classes import BotTarif
with open('tokens.json', 'r') as file:
    data = json.load(file)
token = data['token']
owner = data['owner']
bot_tarif = dict_to_class(data['tarif'], BotTarif)
channels = [-1002013605939]