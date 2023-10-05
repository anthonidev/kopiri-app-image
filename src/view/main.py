import customtkinter
import os
from .setup_images import SetUpImages
from .navigation import Navigation
from .interfaces.web_frame import WebFrame
from .interfaces.config_frame import ConfigFrame
from src.controller.config_actions import ConfigActions


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.title("KOPIRI")
        self.geometry("770x800")
        self.iconbitmap(os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "assets",
            "kopiri_logo.ico"
        ))
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.images = SetUpImages(self)
        self.nav = Navigation(self)
        self.frame_web = WebFrame(self)
        self.frame_config = ConfigFrame(self)

    def change_appearance_mode_event(self, new_appearance_mode):
        config = ConfigActions()
        config.set_theme(new_appearance_mode)
        customtkinter.set_appearance_mode(new_appearance_mode)


def init():
    app = App()
    app.mainloop()
