import json

class CafeManager:
    def __init__(self, file_name="cafe_data.json"):
        self.__file_name = file_name
        self.__cafe_data = self.__read_cafe_file()
    def __read_cafe_file(self):
        with open(self.__file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    def __write_cafe_file(self):
        with open(self.__file_name, "w", encoding="utf-8") as f:
            json.dump(self.__cafe_data, f, ensure_ascii=False, indent=4)
    def run(self):
        pass