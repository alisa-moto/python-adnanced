import json
import os
from json import JSONDecodeError


class ConfigReader:
    def __init__(self, json_file_name):
        self.json_data = self.__json_read_data(json_file_name)
        pass

    def read_param(self, search_key=None, param_key=None):
        all_data = []
        for new_param in self.json_data:
            if search_key in list(new_param.keys()):
                param = new_param[param_key]
                all_data.append(param)
                return all_data.__getitem__(0)

    @staticmethod
    def __json_read_data(json_file_name):
        file_path = os.getcwd() + "\\configs\\" + json_file_name
        try:
            with open(file_path) as file:
                json_data = json.load(file)
                return json_data
        except JSONDecodeError:
            raise Exception
