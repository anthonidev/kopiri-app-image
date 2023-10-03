import tkinter
import tkinter.messagebox
import customtkinter
import os
from .thread import ThreadCompresProcess
from src.model.data import Config
from .functions.select_frame import select_frame_by_name
from .functions.open_files import open_files_action
from utils.image_file import OpenFile
from tkinter import filedialog


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("KOPIRI")
        self.geometry("770x800")
        self.resizable(False, False)

        self.files = []

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        of = OpenFile(
            os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "assets"
            )
        )

        self.logo_image = customtkinter.CTkImage(of.open_image(
            'CustomTkinter_logo_single.png'), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(
            of.open_image("title_image.png"), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(
            of.open_image("image_icon_light.png"),
            size=(20, 20)
        )
        # icons
        self.web_icon = customtkinter.CTkImage(
            light_image=of.open_image("web_dark.png"),
            dark_image=of.open_image("web_light.png"),
            size=(20, 20)
        )
        self.config_icon = customtkinter.CTkImage(
            light_image=of.open_image("config_dark.png"),
            dark_image=of.open_image("config_light.png"),
            size=(20, 20)
        )
        self.upload_icon = customtkinter.CTkImage(
            of.open_image("upload_light.png"),
            size=(20, 20)
        )

        self.compress_icon = customtkinter.CTkImage(
            of.open_image("compress_light.png"),
            size=(15, 15)
        )
        self.clear_icon = customtkinter.CTkImage(
            of.open_image("clear_light.png"),
            size=(15, 15)
        )

        self.file_icon = customtkinter.CTkImage(
            of.open_image("file_light.png"),
            size=(15, 15)
        )

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" KOPIRI", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="WEB",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.web_icon, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="CONFIGURACIÓN",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.config_icon, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(
            row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(5, weight=1)
        # self.home_frame.grid_rowconfigure(6, weight=1)
        self.home_frame_large_image_label = customtkinter.CTkLabel(
            self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(
            row=0, column=0, padx=20, pady=10)

        # button file

        self.button_upload_files = customtkinter.CTkButton(
            self.home_frame,
            text="Seleccionar imagenes",
            image=self.upload_icon, compound="right",
            command=self.open_files,
            font=customtkinter.CTkFont(size=18, weight="bold"),
            hover_color="gray30",
            height=50,
            anchor="center",
        )
        self.button_upload_files.grid(
            row=1, column=0, padx=20, pady=10, sticky="ew")

        # create textbox
        self.text_frame = customtkinter.CTkFrame(
            self.home_frame,
            corner_radius=0,
            fg_color=("gray90", "gray10"),
            border_width=1,
            border_color="gray50"
        )
        self.text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.text_frame.grid_columnconfigure(1, weight=1)
        self.label_upload = customtkinter.CTkLabel(
            self.text_frame,
            font=customtkinter.CTkFont(size=15, weight="normal")
        )
        self.label_upload.grid(
            row=0,
            column=0,
            padx=20,
            pady=5,
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
        self.textbox.grid(row=1, column=0, padx=20, pady=10,
                          sticky="nsew", columnspan=2)

        # quality
        self.quality_frame = customtkinter.CTkFrame(
            self.home_frame, corner_radius=0, fg_color=("gray90", "gray10"), border_width=1, border_color="gray50")

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

        self.sd_quality = customtkinter.CTkSlider(
            self.quality_frame,
            from_=1,
            to=100,
            number_of_steps=100,
            command=self.update_quality,
            width=450

        )
        self.sd_quality.grid(
            row=1,
            column=0,
            padx=20,
            pady=5,
            sticky="w",

        )
        self.lb_quality = customtkinter.CTkLabel(
            self.quality_frame)
        self.lb_quality.grid(
            row=1,
            column=2,
            padx=20,
            pady=5,
            sticky="ew"
        )

        # optimize weight_frame label_weight sd_weight lb_weight

        self.weight_frame = customtkinter.CTkFrame(
            self.home_frame, corner_radius=0, fg_color=("gray90", "gray10"), border_width=1, border_color="gray50")

        self.weight_frame.grid_columnconfigure(1, weight=1)

        self.label_weight = customtkinter.CTkLabel(
            self.weight_frame,
            text="Peso KB",
            font=customtkinter.CTkFont(size=15, weight="normal")
        )
        self.label_weight.grid(
            row=0,
            column=0,
            padx=20,
            pady=5,
            sticky="w",
            columnspan=2
        )

        self.sd_weight = customtkinter.CTkSlider(
            self.weight_frame, from_=1,   width=450, command=self.update_optimize)
        self.sd_weight.grid(row=1, column=0, padx=20, pady=5, sticky="w")
        self.lb_weight = customtkinter.CTkLabel(
            self.weight_frame)
        self.lb_weight.grid(row=1, column=2, padx=20, pady=5, sticky="ew")

        # button compress

        self.action_frame = customtkinter.CTkFrame(
            self.home_frame, corner_radius=0, fg_color="transparent")
        self.action_frame.grid(
            row=5, column=0, padx=20, pady=10, sticky="ew")

        self.action_frame.grid_columnconfigure(1, weight=1)
        self.button_clear_files = customtkinter.CTkButton(
            self.action_frame,
            text="Limpiar",
            command=self.clear_files,
            image=self.clear_icon,
            compound="right",
            font=customtkinter.CTkFont(size=15, weight="bold"),
            hover_color="gray30",
            height=30,
            anchor="center",

        )
        self.button_compress = customtkinter.CTkButton(
            self.action_frame,
            text="Comprimir",
            image=self.compress_icon,
            compound="right",
            command=self.compress,
            font=customtkinter.CTkFont(size=15, weight="bold"),
            hover_color="gray30",
            height=30,
            anchor="center",

        )

        self.button_dir = customtkinter.CTkButton(
            self.action_frame,
            text="Abrir carpeta",
            image=self.file_icon,
            compound="right",
            command=self.open_dir,
            font=customtkinter.CTkFont(size=15, weight="bold"),
            hover_color="gray30",
            height=30,
            anchor="center",
        )

        # loading frame
        self.frame_loading = customtkinter.CTkFrame(
            self.home_frame, corner_radius=0, fg_color=("gray90", "gray10"), border_width=1, border_color="gray50")

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
            row=0, column=1, padx=20, pady=10, sticky="ew")

        self.progress_bar.grid(
            row=0, column=0, padx=20, pady=10, sticky="ew")

        # create second frame
        self.second_frame = customtkinter.CTkFrame(
            self, corner_radius=0, fg_color="transparent")

        self.output_frame = customtkinter.CTkFrame(
            self.second_frame, corner_radius=0, fg_color=("gray90", "gray10"))
        self.output_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ew")
        self.output_frame.grid_rowconfigure(0, weight=1)
        self.output_frame.grid_columnconfigure(0, weight=1)

        self.output_frame_label = customtkinter.CTkLabel(
            self.output_frame, text="Ruta donde se guardaran los archivos")
        self.output_frame_label.grid(
            row=0, column=0, padx=20, pady=10, sticky="ew")

        self.output_frame_textbox = customtkinter.CTkEntry(
            self.output_frame, width=500)
        self.output_frame_textbox.grid(
            row=1, column=0, padx=20, pady=10, sticky="nsew")

        self.output_frame_button = customtkinter.CTkButton(
            self.output_frame, text="Seleccionar carpeta", command=self.select_dir)
        self.output_frame_button.grid(
            row=2, column=0, padx=20, pady=10, sticky="ew")

        # quality default
        self.quality_config_frame = customtkinter.CTkFrame(
            self.second_frame, corner_radius=0, fg_color=("gray90", "gray10"))
        self.quality_config_frame.grid(
            row=1, column=0, padx=20, pady=10, sticky="ew")
        self.quality_config_frame.grid_rowconfigure(0, weight=1)
        self.quality_config_frame.grid_columnconfigure(1, weight=1)

        self.quality_config_frame_label = customtkinter.CTkLabel(
            self.quality_config_frame, text="Calidad por defecto", width=100)
        self.quality_config_frame_label.grid(
            row=0, column=0, padx=20, pady=10, sticky="ew")

        self.quality_config_frame_textbox = customtkinter.CTkEntry(
            self.quality_config_frame, width=300)
        self.quality_config_frame_textbox.grid(
            row=0, column=1, padx=20, pady=10, sticky="nsew")

        # weight default

        self.weight_config_frame = customtkinter.CTkFrame(
            self.second_frame, corner_radius=0, fg_color=("gray90", "gray10"))
        self.weight_config_frame.grid(
            row=2, column=0, padx=20, pady=10, sticky="ew")

        self.weight_config_frame_label = customtkinter.CTkLabel(
            self.weight_config_frame, text="Peso por defecto (KB)", width=100)
        self.weight_config_frame_label.grid(
            row=0, column=0, padx=20, pady=10, sticky="ew")

        self.weight_config_frame_textbox = customtkinter.CTkEntry(
            self.weight_config_frame, width=300)
        self.weight_config_frame_textbox.grid(
            row=0, column=1, padx=20, pady=10, sticky="nsew")

        self.weight_max_config_frame_label = customtkinter.CTkLabel(
            self.weight_config_frame, text="Peso maximo por defecto (KB)", width=100)
        self.weight_max_config_frame_label.grid(
            row=1, column=0, padx=20, pady=10, sticky="ew")

        self.weight_max_config_frame_textbox = customtkinter.CTkEntry(
            self.weight_config_frame, width=300)
        self.weight_max_config_frame_textbox.grid(
            row=1, column=1, padx=20, pady=10, sticky="nsew")

        # button save config

        self.save_config_frame = customtkinter.CTkFrame(
            self.second_frame, corner_radius=0, fg_color="transparent")

        self.save_config_frame.grid(
            row=3, column=0, padx=20, pady=10, sticky="ew")
        self.save_config_frame.grid_rowconfigure(0, weight=1)
        self.save_config_frame.grid_columnconfigure(1, weight=1)

        self.button_default_config = customtkinter.CTkButton(
            self.save_config_frame, text="Restablecer", command=self.default_config)
        self.button_default_config.grid(
            row=0, column=0, padx=20, pady=10, sticky="ew")

        self.button_save_config = customtkinter.CTkButton(
            self.save_config_frame, text="Guardar configuración", command=self.save_config)
        self.button_save_config.grid(
            row=0, column=1, padx=20, pady=10, sticky="ew")

        # select default frame and read config
        self.select_frame_by_name("home")
        self.read_config()
        self.apply_config()
        self.clear_files()

    def clear_files(self):
        self.button_upload_files.grid(
            row=1, column=0, padx=20, pady=10, sticky="ew")
        self.text_frame.grid_forget()
        self.quality_frame.grid_forget()
        self.action_frame.grid_forget()
        self.frame_loading.grid_forget()
        self.weight_frame.grid_forget()
        self.progress_bar.grid_forget()
        self.label_progress_bar.grid_forget()
        self.button_compress.grid_forget()
        self.button_clear_files.grid_forget()
        self.button_dir.grid_forget()
        self.files = []

    def clear_config(self):
        self.output_frame_textbox.delete(0, tkinter.END)
        self.quality_config_frame_textbox.delete(0, tkinter.END)
        self.weight_config_frame_textbox.delete(0, tkinter.END)
        self.weight_max_config_frame_textbox.delete(0, tkinter.END)

    def read_config(self):
        config = Config()
        if config.get_manipulation() == False:
            # default output dir is download folder
            config.set_output_dir(os.path.join(
                os.path.expanduser("~"), "Downloads"))
            config.set_manipulation(True)
        self.output_frame_textbox.insert(
            0, config.get_output_dir())

        self.quality_config_frame_textbox.insert(
            0, config.get_quality())

        self.weight_config_frame_textbox.insert(
            0, config.get_weight())
        self.weight_max_config_frame_textbox.insert(
            0, config.get_weight_max())

        self.change_appearance_mode_event(config.get_theme())

    def apply_config(self):
        self.sd_quality.set(int(self.quality_config_frame_textbox.get()))
        self.lb_quality.configure(text=str(
            self.quality_config_frame_textbox.get()))

        self.sd_weight.configure(
            from_=100, to=int(self.weight_max_config_frame_textbox.get()), number_of_steps=int(self.weight_max_config_frame_textbox.get()) / 10
        )

        self.sd_weight.set(int(self.weight_config_frame_textbox.get()))
        self.lb_weight.configure(text=str(
            self.weight_config_frame_textbox.get()))

    def open_files(self):
        open_files_action(self)

    def show_frames(self):
        self.text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.quality_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.weight_frame.grid(
            row=4, column=0, padx=20, pady=10, sticky="ew")
        self.action_frame.grid(
            row=5, column=0, padx=20, pady=10, sticky="ew")

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

    def select_frame_by_name(self, name):
        select_frame_by_name(self, name)

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def change_appearance_mode_event(self, new_appearance_mode):
        config = Config()
        config.set_theme(new_appearance_mode)
        customtkinter.set_appearance_mode(new_appearance_mode)

    def compress(self):
        self.quality_frame.grid_forget()
        self.action_frame.grid_forget()
        self.weight_frame.grid_forget()
        self.button_compress.grid_forget()

        self.frame_loading.grid(
            row=6, column=0, padx=20, pady=10, sticky="ew")
        thread = ThreadCompresProcess(
            files=self.files,
            quality=int(self.sd_quality.get()),
            weight_max=int(self.sd_weight.get()),
            progress_bar=self.progress_bar,
            label_progress_bar=self.label_progress_bar,
            output_dir=self.output_frame_textbox.get(),
            textbox=self.textbox,
            frame=self.frame_loading,
            button_compress=self.button_compress,
            button_dir=self.button_dir,
            action_frame=self.action_frame

        )
        thread.start()

    def save_config(self):
        config = Config()
        config.set_output_dir(self.output_frame_textbox.get())
        config.set_quality(self.quality_config_frame_textbox.get())
        config.set_weight(self.weight_config_frame_textbox.get())
        config.set_weight_max(self.weight_max_config_frame_textbox.get())
        self.clear_config()
        self.read_config()
        self.apply_config()
        tkinter.messagebox.showinfo(
            "Información", "Configuración guardada correctamente")

    def default_config(self):
        config = Config()
        config.default_config()
        self.clear_config()
        self.read_config()
        self.apply_config()
        tkinter.messagebox.showinfo(
            "Información", "Configuración restablecida correctamente")

    def open_dir(self):
        output_dir = self.output_frame_textbox.get()
        os.startfile(output_dir)

    def select_dir(self):
        output_dir = filedialog.askdirectory()
        if output_dir != "":
            self.output_frame_textbox.delete(0, tkinter.END)
            self.output_frame_textbox.insert(0, output_dir + "/")
        else:
            pass


def init():
    app = App()
    app.mainloop()
