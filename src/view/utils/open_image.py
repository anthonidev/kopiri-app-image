from PIL import Image
import os


class OpenFile():
    def __init__(self, file):
        self.image_path = file

    def open_image(self, file):
        return Image.open(os.path.join(self.image_path, file))
