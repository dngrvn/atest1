import json
from Path import Path
from Printer import Printer
from TxtInterface import TxtInterface


class Export_json:
    def __init__(self, data):
        self.data = data
        self.writeabled = {}

    def write(self):
        if len(self.data) > 0:
            self.writeabled['Note'] = []
            for item in self.data:
                self.writeabled['Note'].append({
                    'Title': item.title,
                    'Note': item.body,
                    'Date': item.date_create,
                    'ID': item.id_note
                })
            with open(Path.PATH_JSON, 'w') as sender:
                json.dump(self.writeabled, sender)
            Printer(TxtInterface().notes_saved).prints()
        else:
            Printer(TxtInterface().notes_empty).prints()
