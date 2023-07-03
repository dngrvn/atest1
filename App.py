import os

from Add_note import Add_new_note
from Database import Database
from Deleter import Deleter
from Editor import Editor
from Export_json import Export_json
from Import_json import Import_json
from Path import Path
from Printer import Printer
from Show_data import Show_data
from TxtInterface import TxtInterface


class App(object):
    def main(self):
        alpha = Database("alpha")
        flag = True
        Printer(TxtInterface().greeting).prints()
        while (flag):
            Printer(TxtInterface().first_menu).prints()
            command = input(TxtInterface().enter_command)
            if command == "1":
                adder = Add_new_note()
                adder.add_note()
                alpha.dbase.append(adder.note)
                Printer(TxtInterface().not_save).prints()
            elif command == "2":
                appearance = Show_data(alpha.dbase)
                appearance.show()
            elif command == "3":
                shower = Show_data(alpha.dbase)
                shower.show_last_note()
            elif command == "4":
                editor = Editor(alpha.dbase)
                editor.edit()
            elif command == "5":
                deleter = Deleter(alpha.dbase)
                deleter.delete()
            elif command == "6":
                if os.path.isfile(Path.PATH_JSON):
                    exporter = Export_json(alpha.dbase)
                    exporter.write()
                else:
                    Printer(TxtInterface.not_file).prints()
            elif command == "7":
                if os.path.isfile(Path.PATH_JSON):
                    importer = Import_json()
                    importer.read_file()
                    importer.parse_input()
                    alpha.dbase = importer.parse_data
                else:
                    Printer(TxtInterface.not_file).prints()
            elif command == "0":
                Printer(TxtInterface().goodbye).prints()
                flag = False
            else:
                Printer(TxtInterface().incorrect_input).prints()
