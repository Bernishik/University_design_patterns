from lxml import etree

from JsonRequestAdapter import JsonRequestAdapter


class WebClient:
    def __init__(self):
        self.create_attachment()

    def create_attachment(self):
        self.i_web_request = JsonRequestAdapter()

    def upload(self, name: str, last_name: str, age: int, text: str):
        x_root = etree.Element("root")
        x_name = etree.SubElement(x_root, "name")
        x_lastname = etree.SubElement(x_root, "lastname")
        x_age = etree.SubElement(x_root, "age")
        x_txt = etree.SubElement(x_root, "txt")
        x_name.text = name
        x_lastname.text = last_name
        x_age.text = str(age)
        x_txt.text = text

        xml = etree.tostring(x_root, xml_declaration=True, encoding="utf-8")
        self.i_web_request.request(xml)

        return True
