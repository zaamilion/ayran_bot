import json

class Database:
    def __init__(self, file_name):
        self.file_name = file_name
        self.list = []
    def dump(self):
        with open(f'{self.file_name}.json', 'w') as file:
            json.dump(self.list, file)
    def load(self):
        with open(f'{self.file_name}.json', 'r') as file:
            self.list = json.load(file)
            return self.list