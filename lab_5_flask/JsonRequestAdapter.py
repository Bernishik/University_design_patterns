import xmltodict

from IWebRequest import IWebRequest
from WebServices import WebServices
import  json


class JsonRequestAdapter(IWebRequest):
    def __init__(self):
        self.connect()

    def request(self, obj) -> bool:
        j = self.xml_to_json(obj)
        return self.web_services.post_request(j)


    def connect(self):
        self.web_services = WebServices()

    def xml_to_json(self, xml):
        data = xmltodict.parse(xml)
        result = json.dumps(data)
        return result
