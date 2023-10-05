import customtkinter
from src.controller.open_files_action import OpenFilesAction
from src.controller.thread_compress import ThreadCompresProcess
import os


class WebFrame():
    def __init__(self, master):
        self.master = master
        self.web_frame = master.web_frame
        self.files = []
        self.web_ui()

    def web_ui(self):
        self.banner = customtkinter.CTkLabel(
            self.web_frame, text="", image=self.master.banner_image_web)

        self.button_upload_files = customtkinter.CTkButton(
            self.web_frame,
            text="Seleccionar imagenes",
            image=self.master.upload_icon,
            compound="right",
            font=customtkinter.CTkFont(size=18, weight="bold"),
            hover_color="gray30",
            height=50, anchor="center",
            command=self.open_files,
        )

        self.banner.grid(
            row=0, column=0,
            padx=20, pady=10
        )
        self.button_upload_files.grid(
            row=1, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.text_frame_ui()
        self.quality_frame_ui()
        self.weight_frame_ui()
        self.action_frame_ui()
        self.frame_loading_ui()

    def text_frame_ui(self):
        self.text_frame = customtkinter.CTkFrame(
            self.web_frame,
            corner_radius=0,
            fg_color=("gray90", "gray10"),
            border_width=1,
            border_color="gray50"
        )
        self.text_frame.grid_columnconfigure(1, weight=1)
        self.label_upload = customtkinter.CTkLabel(
            self.text_frame,
            font=customtkinter.CTkFont(size=15, weight="normal")
        )
        self.label_upload.grid(
            row=0, column=0,
            padx=20, pady=5,
            sticky="e"
        )

        self.label_supported = customtkinter.CTkLabel(
            self.text_frame,
            font=customtkinter.CTkFont(size=15, weight="normal")
        )
        self.label_supported.grid(
            row=0,
            column=1,
            padx=20,
            pady=5,
            sticky="w"
        )
        self.textbox = customtkinter.CTkTextbox(self.text_frame, width=500)
        self.textbox.grid(
            row=1, column=0,
            padx=20, pady=10,
            sticky="nsew", columnspan=2
        )

    def quality_frame_ui(self):
        self.quality_frame = customtkinter.CTkFrame(
            self.web_frame,
            corner_radius=0,
            fg_color=("gray90", "gray10"),
            border_width=1, border_color="gray50"
        )
        self.quality_frame.grid_columnconfigure(1, weight=1)

        self.label_quality = customtkinter.CTkLabel(
            self.quality_frame,
            text="Calidad",
            font=customtkinter.CTkFont(size=15, weight="normal")
        )
        self.label_quality.grid(
            row=0,
            column=0,
            padx=20,
            pady=5,
            sticky="w",
            columnspan=2
        )
        self.master.sd_quality = customtkinter.CTkSlider(
            self.quality_frame,
            from_=1,
            to=100,
            number_of_steps=100,
            command=self.update_quality,
            width=450

        )
        self.sd_quality = self.master.sd_quality
        self.sd_quality.grid(
            row=1,
            column=0,
            padx=20,
            pady=5,
            sticky="w",

        )
        self.master.lb_quality = customtkinter.CTkLabel(
            self.quality_frame)
        self.lb_quality = self.master.lb_quality
        self.lb_quality.grid(
            row=1,
            column=2,
            padx=20,
            pady=5,
            sticky="ew"
        )

    def weight_frame_ui(self):
        self.weight_frame = customtkinter.CTkFrame(
            self.web_frame,
            corner_radius=0,
            fg_color=("gray90", "gray10"),
            border_width=1,
            border_color="gray50"
        )
        self.weight_frame.grid_columnconfigure(1, weight=1)
        self.label_weight = customtkinter.CTkLabel(
            self.weight_frame,
            text="Peso KB",
            font=customtkinter.CTkFont(size=15, weight="normal")
        )
        self.label_weight.grid(
            row=0, column=0,
            padx=20, pady=5,
            sticky="w", columnspan=2
        )
        self.master.sd_weight = customtkinter.CTkSlider(
            self.weight_frame, from_=1,
            width=450,
            command=self.update_optimize
        )
        self.sd_weight = self.master.sd_weight
        self.sd_weight.grid(
            row=1, column=0,
            padx=20, pady=5,
            sticky="w"
        )
        self.master.lb_weight = customtkinter.CTkLabel(
            self.weight_frame)
        self.lb_weight = self.master.lb_weight
        self.lb_weight.grid(row=1, column=2, padx=20, pady=5, sticky="ew")

    def action_frame_ui(self):
        self.action_frame = customtkinter.CTkFrame(
            self.web_frame,
            corner_radius=0,
            fg_color="transparent"
        )
        self.action_frame.grid(
            row=5, column=0,
            padx=20, pady=10,
            sticky="ew"
        )
        self.action_frame.grid_columnconfigure(1, weight=1)

        self.button_clear_files = customtkinter.CTkButton(
            self.action_frame,
            text="Limpiar",
            image=self.master.clear_icon,
            compound="right",
            font=customtkinter.CTkFont(size=15, weight="bold"),
            hover_color="gray30",
            height=30,
            anchor="center",
            command=self.clear_files,
        )
        self.button_compress = customtkinter.CTkButton(
            self.action_frame,
            text="Comprimir",
            image=self.master.compress_icon,
            compound="right",
            font=customtkinter.CTkFont(size=15, weight="bold"),
            hover_color="gray30",
            height=30,
            anchor="center",
            command=self.compress,
        )

        self.button_dir = customtkinter.CTkButton(
            self.action_frame,
            text="Abrir carpeta",
            image=self.master.file_icon,
            compound="right",
            font=customtkinter.CTkFont(size=15, weight="bold"),
            hover_color="gray30",
            height=30,
            anchor="center",
            command=self.open_dir,
        )

    def frame_loading_ui(self):
        self.frame_loading = customtkinter.CTkFrame(
            self.web_frame, corner_radius=0,
            fg_color=("gray90", "gray10"),
            border_width=1, border_color="gray50"
        )
        self.frame_loading.grid_columnconfigure(1, weight=1)

        self.progress_bar = customtkinter.CTkProgressBar(
            self.frame_loading,
            width=400,
            mode="determinate",
        )
        self.label_progress_bar = customtkinter.CTkLabel(
            self.frame_loading,
            text="100%",
            font=customtkinter.CTkFont(size=15, weight="normal")
        )
        self.label_progress_bar.grid(
            row=0, column=1,
            padx=20, pady=10,
            sticky="ew"
        )

        self.progress_bar.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

    def update_quality(self, event):
        value = self.sd_quality.get()
        value = int(value)
        self.lb_quality.configure(
            text=str(value))

    def update_optimize(self, event):
        value = self.sd_weight.get()
        value = int(value)
        self.lb_weight.configure(
            text=str(value))

    def show_frames(self):
        self.text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.quality_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.weight_frame.grid(
            row=4, column=0, padx=20, pady=10, sticky="ew")
        self.action_frame.grid(
            row=5, column=0, padx=20, pady=10, sticky="ew")

    def hide_frames(self, compress: bool = False):

        self.quality_frame.grid_forget()
        self.weight_frame.grid_forget()
        self.action_frame.grid_forget()
        if compress == False:
            self.text_frame.grid_forget()
            self.button_dir.grid_forget()

        else:
            self.frame_loading.grid(
                row=6, column=0,
                padx=20, pady=10,
                sticky="ew"
            )
            self.progress_bar.grid(
                row=6, column=0, padx=20, pady=10, sticky="ew")
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", "end")
            self.textbox.configure(state="disabled")

    def open_files(self):
        files_action = OpenFilesAction()
        if files_action.response:
            self.show_frames()
            self.files = files_action.supported_files_list

            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", "end")
            text = "\n".join(self.files)
            self.textbox.insert("0.0", text)
            self.textbox.see("end")
            self.textbox.configure(state="disabled")

            self.label_upload.configure(
                text="Archivos subidos (" +
                str(files_action.suploaded_files_counter()) + ")"
            )
            self.label_supported.configure(
                text="Archivos soportados (" +
                str(files_action.supported_files_counter()) + ")"
            )

            self.button_clear_files.grid(
                row=0, column=0,
                padx=20, pady=10,
                sticky="ew"
            )
            self.button_compress.grid(
                row=0, column=1,
                padx=20, pady=10,
                sticky="ew"
            )

            self.button_upload_files.grid_forget()

    def clear_files(self):
        self.button_upload_files.grid(
            row=1, column=0, padx=20, pady=10, sticky="ew")
        self.hide_frames()
        self.files = []

    def compress(self):
        self.hide_frames(True)
        thread = ThreadCompresProcess(self)
        thread.start()

    def open_dir(self):
        output_dir = self.master.output_frame_textbox.get()
        os.startfile(output_dir)
