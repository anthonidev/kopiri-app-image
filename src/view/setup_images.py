import customtkinter
import os
from .utils.open_image import OpenFile


class SetUpImages:
    def __init__(self, master):
        self.master = master
        self.path = OpenFile(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "assets"
            )
        )

        self.load_images()

    def load_images(self):
        self.master.logo_image = customtkinter.CTkImage(
            self.path.open_image('kopiri_logo.png'),
            size=(26, 26)
        )

        self.master.banner_image_web = customtkinter.CTkImage(
            self.path.open_image("banner_image_web.png"),
            size=(500, 150)
        )

        self.master.banner_image_config = customtkinter.CTkImage(
            self.path.open_image("banner_image_config.png"),
            size=(500, 150)
        )

        self.master.web_icon = customtkinter.CTkImage(
            light_image=self.path.open_image("web_dark.png"),
            dark_image=self.path.open_image("web_light.png"),
            size=(20, 20)
        )

        self.master.config_icon = customtkinter.CTkImage(
            light_image=self.path.open_image("config_dark.png"),
            dark_image=self.path.open_image("config_light.png"),
            size=(20, 20)
        )

        self.master.upload_icon = customtkinter.CTkImage(
            self.path.open_image("upload_light.png"),
            size=(20, 20)
        )

        self.master.compress_icon = customtkinter.CTkImage(
            self.path.open_image("compress_light.png"),
            size=(15, 15)
        )

        self.master.clear_icon = customtkinter.CTkImage(
            self.path.open_image("clear_light.png"),
            size=(15, 15)
        )

        self.master.file_icon = customtkinter.CTkImage(
            self.path.open_image("file_light.png"),
            size=(15, 15)
        )
