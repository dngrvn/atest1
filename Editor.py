from Input_data import Input_console_data
from Printer import Printer
from Show_data import Show_data
from TxtInterface import TxtInterface


class Editor():
    def __init__(self, edition):
      self.edition = edition

    def edit(self):
        if len(self.edition) > 0:
            editor = Show_data(self.edition)
            editor.show()
            titler = Input_console_data()
            titler.input_data(TxtInterface.edit_note)
            temp = list(filter(lambda x: x.title.count(titler.input), self. edition)) # type: ignore
            for item in temp:
               Printer(TxtInterface.current_title).prints()
               Printer(item.title).prints()
               titler.input_data(TxtInterface.enter_title)
               item.title = titler.input
               Printer(TxtInterface.current_note).prints()
               Printer(item.body).prints()
               titler.input_data(TxtInterface.enter_note)
               item.body = titler.input
        else:
           Printer(TxtInterface.notes_empty).prints()