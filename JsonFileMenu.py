from AbstractFileMenu import AbstractFileMenu
import json


class JsonFileMenu(AbstractFileMenu):
    def __init__(self):
        super().__init__()
        self.buttons[1] = "Write json object"

    def write_to_file(self):
        ss = self.get_some_struct()

        f = open(input("Enter filename: "), "w+")
        f.write(json.dumps(ss.__dict__))
        f.close()