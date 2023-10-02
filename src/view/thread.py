
from threading import Thread
from src.controller.compress_kopiri import compress_kopiri
import tkinter


class ThreadCompresProcess(Thread):
    def __init__(self, files, quality, weight_max, progress_bar):
        Thread.__init__(self)
        self.files = files
        self.quality = quality
        self.weight_max = weight_max * 1000
        self.progress_bar = progress_bar

    def run(self):
        self.progress_bar.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        self.progress_bar.start()
        compress_kopiri(
            self.files,
            self.quality,
            self.weight_max
        )
        tkinter.messagebox.showinfo(
            "Compress", "Compressing " + str(len(self.files)) + " images")
        self.progress_bar.stop()
        self.progress_bar.grid_forget()
        self.progress_bar.stop()
        print("Thread finished")
