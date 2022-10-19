from AbstractFileMenu import AbstractFileMenu
import xml.etree.ElementTree as ET


class XMLFileMenu(AbstractFileMenu):
    def __init__(self):
        super().__init__()
        self.buttons[1] = "Write xml object"

    def write_to_file(self):
        ss = self.get_some_struct()

        data = ET.Element("some_struct")

        id_element = ET.SubElement(data, "id")
        id_element.text = str(ss.id)

        name_element = ET.SubElement(data, "name")
        name_element.text = ss.name

        some_doubles_element = ET.SubElement(data, "some_doubles")
        for some_double in ss.some_doubles:
            some_double_element = ET.SubElement(some_doubles_element, "some_double")
            some_double_element.text = str(some_double)

        f = open(input("Enter filename: "), "w+")
        f.write(ET.tostring(data).decode())
        f.close()