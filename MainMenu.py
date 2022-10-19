from consolemenu import *
from consolemenu.items import *

from DiskInfoMenu import DiskInfoMenu
from TextFileMenu import TextFileMenu
from JsonFileMenu import JsonFileMenu
from XMLFileMenu import XMLFileMenu
from ZipMenu import ZipMenu


class MainMenu:
    def __init__(self):
        self.program_name = "Safe Software"
        self.text_menu = TextFileMenu()
        self.json_menu = JsonFileMenu()
        self.xml_menu = XMLFileMenu()
        self.zip_menu = ZipMenu()
        menu = self.create_menu()
        menu.show()

    def create_menu(self):
        menu = ConsoleMenu(self.program_name, "Lab1")

        menu.append_item(FunctionItem("Get logic disks info", self.print_disk_info))
        menu.append_item(SubmenuItem("Text file", self.create_sub_menu("Text", self.text_menu)))
        menu.append_item(SubmenuItem("Json file", self.create_sub_menu("Json", self.json_menu)))
        menu.append_item(SubmenuItem("Xml file", self.create_sub_menu("Xml", self.xml_menu)))
        menu.append_item(SubmenuItem("Zip file", self.create_sub_menu("Zip", self.zip_menu)))
        return menu

    def create_sub_menu(self, name, sub_menu_obj):
        sub_menu = ConsoleMenu(self.program_name, name + " file")

        create_file_function_item = FunctionItem(sub_menu_obj.buttons[0], sub_menu_obj.create_file)
        write_obj_to_file_function_item = FunctionItem(sub_menu_obj.buttons[1], sub_menu_obj.write_to_file)
        read_text_from_file_function_item = FunctionItem(sub_menu_obj.buttons[2], sub_menu_obj.read_all_file)
        delete_file_function_item = FunctionItem(sub_menu_obj.buttons[3], sub_menu_obj.delete_file)

        sub_menu.append_item(create_file_function_item)
        sub_menu.append_item(write_obj_to_file_function_item)
        sub_menu.append_item(read_text_from_file_function_item)
        sub_menu.append_item(delete_file_function_item)

        return sub_menu

    def print_disk_info(self):
        DiskInfoMenu.get_disk_info()
