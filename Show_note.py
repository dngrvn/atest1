class Show_note:
    def __init__(self, note):
        self.note = note

    def printNote(self):
        return "Date: {}\nTitle: {}\nNote: {}\nID: {}\n".format(self.note.date_create,
                                                                self.note.title, self.note.body, self.note.id_note)
