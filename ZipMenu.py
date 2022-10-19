from AbstractFileMenu import AbstractFileMenu
import os
import zipfile


class ZipMenu(AbstractFileMenu):
    def __init__(self):
        super().__init__()
        self.buttons[0] = "Create zip archive"
        self.buttons[1] = "Add file to zip archive"
        self.buttons[2] = "Get file from zip archive"
        self.buttons[3] = "Delete zip archive"

    def create_file(self):
        f = zipfile.ZipFile(input("Enter filename: "), "w")
        f.close()

    def write_to_file(self):
        f = zipfile.ZipFile(input("Enter archive name: "), "a")
        path_to_file = input("Enter filename: ")
        f.write(path_to_file, os.path.basename(path_to_file))
        f.close()

    def read_all_file(self):
        archive = zipfile.ZipFile(input("Enter archive name: "), "r")

        filename = input("Enter filename: ")
        data = archive.read(filename)
        archive.close()

        f = open(filename, "w+b")
        f.write(data)
        f.close()

        print("size:", os.path.getsize(filename))
        print("modify timestamp:", os.path.getmtime(filename))
        input()