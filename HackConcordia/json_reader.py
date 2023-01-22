import json
import qrcode


class JSONFileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as f:
            json_data = json.load(f)
            self.contents = json.dumps(json_data)
        return self.contents