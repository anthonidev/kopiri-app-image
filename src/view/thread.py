
from threading import Thread
from src.controller.compress_kopiri import compress_kopiri
import tkinter


class ThreadCompresProcess(Thread):
    def __init__(
        self,
        files,
        quality,
        weight_max,
        progress_bar,
        label_progress_bar,
        output_dir,
        textbox,
        frame,
        button_compress,
        button_dir,
        action_frame,
    ):
        Thread.__init__(self)
        self.files = files
        self.quality = quality
        self.weight_max = weight_max * 1000
        self.progress_bar = progress_bar
        self.output_dir = output_dir
        self.label_progress_bar = label_progress_bar
        self.textbox = textbox
        self.frame = frame
        self.button_compress = button_compress
        self.button_dir = button_dir
        self.action_frame = action_frame

    def run(self):

        self.progress_bar.grid(row=6, column=0, padx=20, pady=10, sticky="ew")
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        self.textbox.configure(state="disabled")
        compress_kopiri(
            self.files,
            self.quality,
            self.weight_max,
            self.output_dir,
            self.progress_bar,
            self.label_progress_bar,
            self.textbox
        )
        tkinter.messagebox.showinfo(
            "Compress", "Compressing " + str(len(self.files)) + " images")
        self.progress_bar.grid_forget()
        self.progress_bar.stop()
        self.frame.grid_forget()

        self.action_frame.grid(
            row=5, column=0, padx=20, pady=10, sticky="ew")
        self.button_compress.grid_forget()

        self.button_dir.grid(
            row=0, column=1, padx=20, pady=10, sticky="ew")
