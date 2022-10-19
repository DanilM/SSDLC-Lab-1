from AbstractFileMenu import AbstractFileMenu


class TextFileMenu(AbstractFileMenu):
    def __init__(self):
        super().__init__()
        self.buttons[1] = "Write text"

    def write_to_file(self):
        f = open(input("Enter filename: "), "w+")
        f.write(input("Enter text: "))
        f.close()