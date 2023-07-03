import json
from Note import Note
from Path import Path
from Printer import Printer
from TxtInterface import TxtInterface


class Import_json:
    def __init__(self):
        self.input_data = []

    def read_file(self):
        with open(Path.PATH_JSON) as json_file:
            self.input_data = json.load(json_file)
            Printer(TxtInterface().notes_imported).prints()

    def parse_input(self):
        self.parse_data = []
        for item in self.input_data['Note']:
            note = Note()
            note.set(item['ID'], item['Title'], item['Note'], item['Date'])
            self.parse_data.append(note)