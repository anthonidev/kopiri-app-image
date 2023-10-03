import json
import os

file_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(file_path, "..", "..", "config.json")


def read_json():
    with open(file_path) as json_file:
        data = json.load(json_file)
        return data


def write_json(data):
    with open(file_path, 'w') as outfile:
        json.dump(data, outfile, indent=4)


def default_config():
    data = {
        "quality": "60",
        "weight_max": "700",
        # default output dir is download folder
        "output_dir": os.path.join(os.path.expanduser("~"), "Downloads"),
        "weight": "350",
        "theme": "System",
        "manipulation": True
    }
    write_json(data)


class Config():
    def __init__(self):

        self.data = read_json()

    def get_manipulation(self):
        return self.data["manipulation"]

    def get_quality(self):
        return self.data["quality"]

    def get_weight_max(self):
        return self.data["weight_max"]

    def get_output_dir(self):
        return self.data["output_dir"]

    def get_weight(self):
        return self.data["weight"]

    def get_theme(self):
        return self.data["theme"]

    def set_quality(self, quality):
        self.data["quality"] = quality
        write_json(self.data)

    def set_weight_max(self, weight_max):
        self.data["weight_max"] = weight_max
        write_json(self.data)

    def set_output_dir(self, output_dir):
        self.data["output_dir"] = output_dir
        write_json(self.data)

    def set_weight(self, weight):
        self.data["weight"] = weight
        write_json(self.data)

    def set_theme(self, theme):
        self.data["theme"] = theme
        write_json(self.data)

    def set_manipulation(self, manipulation):
        self.data["manipulation"] = manipulation
        write_json(self.data)

    def default_config(self):
        default_config()
        self.data = read_json()
