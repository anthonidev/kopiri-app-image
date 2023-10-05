
from threading import Thread
import tkinter
from .compress_web import CompressWeb
from src.model.config import Config


class ThreadCompresProcess(Thread):
    def __init__(
        self,
        master,
    ):
        Thread.__init__(self)
        self.master = master
        self.output_dir = Config().get_output_dir()

    def run(self):

        CompressWeb(
            self.master.files,
            int(self.master.sd_quality.get()),
            int(self.master.sd_weight.get()),
            self.output_dir,
            self.master.progress_bar,
            self.master.label_progress_bar,
            self.master.textbox
        )

        tkinter.messagebox.showinfo(
            "Compress", "Compressing " + str(len(self.master.files)) + " images")
        self.master.progress_bar.grid_forget()
        self.master.progress_bar.stop()
        self.master.frame_loading.grid_forget()

        self.master.action_frame.grid(
            row=5, column=0, padx=20, pady=10, sticky="ew")
        self.master.button_compress.grid_forget()

        self.master.button_dir.grid(
            row=0, column=1, padx=20, pady=10, sticky="ew")
