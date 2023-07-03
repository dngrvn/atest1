from Input_data import Input_console_data
from TxtInterface import TxtInterface


class Input_console_note:
    def __init__(self):
      self.title = TxtInterface().is_empty
      self.body = TxtInterface().is_empty

    def input_note(self):
        input_user = Input_console_data()
        input_user.input_data(TxtInterface().enter_title)
        self.title = input_user.input
        input_user.input_data(TxtInterface().enter_note)
        self.body = input_user.input