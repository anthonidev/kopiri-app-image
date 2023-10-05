from src.model.config import Config
import os


class ConfigActions():
    def __init__(self):
        self.config = Config()
        self.default_path = os.path.join(os.path.expanduser("~"), "Downloads")

    def get_config_value(self, key):
        return self.config.data.get(key)

    def set_config_value(self, key, value):
        if key in self.config.data:
            self.config.data[key] = value
            self.config.write_json(self.config.data)

    def set_init_app(self):
        if self.config.get_manipulation() == False:
            self.config.set_output_dir(self.default_path)
            self.config.set_manipulation(True)
        else:
            pass

    def default_config(self):
        self.config.default_config()

    def save_config(self, output_dir, quality, weight, weight_max):
        self.config.set_output_dir(output_dir)
        self.config.set_quality(quality)
        self.config.set_weight(weight)
        self.config.set_weight_max(weight_max)

    def set_theme(self, theme):
        self.config.set_theme(theme)
