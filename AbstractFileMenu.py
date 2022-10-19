import os
import random


class AbstractFileMenu:
    def __init__(self):
        self.buttons = ["Create file", "Write file", "Read text", "Delete file"]

    def create_file(self):
        f = open(input("Enter filename: "), "w+")
        f.close()

    def read_all_file(self):
        f = open(input("Enter filename: "), "r")
        print(f.read())
        f.close()
        input()

    def delete_file(self):
        os.remove(input("Enter filename: "))

    def write_to_file(self):
        return

    class some_struct:
        def __init__(self, id, name, some_doubles):
            self.id = id
            self.name = name
            self.some_doubles = some_doubles

    def get_some_struct(self):
        id = int(input("id = "))
        name = input("name = ")
        some_doubles = []
        for i in range(0, 5):
            some_doubles.append(random.random())

        return self.some_struct(id, name, some_doubles)