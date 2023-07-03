from Input_data import Input_console_data
from Printer import Printer
from Show_data import Show_data
from TxtInterface import TxtInterface


class Deleter:
    def __init__(self, cookies):
        self.cookies = cookies

    def delete(self):
        if len(self.cookies) > 0:
            shower = Show_data(self.cookies)
            shower.show()
            number = Input_console_data()
            number.input_data(TxtInterface.enter_ID)
            find = None
            for note in range(len(self.cookies)):
                if self.cookies[note].id_note == int(number.input):
                    find = note
                    break
            self.cookies.pop(find)
            Printer(TxtInterface.note_deleted).prints()
        else:
            Printer(TxtInterface.notes_empty).prints()