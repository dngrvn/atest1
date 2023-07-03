from datetime import datetime

from TxtInterface import TxtInterface


class Note:
    id = 0

    def __init__(self):
       self.id_note = Note.id + 1
       self.title = TxtInterface.is_empty
       self.body = TxtInterface.is_empty
       self.date_create = str(datetime.now())
       Note.id +=1

    def set(self, id, title, body, date):
        self.id_note = id
        self.title = title
        self.body = body
        self.date_create = str(date)
        if int(id) > Note.id:
            Note.id = int(id)
