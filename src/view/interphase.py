from src.model.data import Config
from .functions.select_frame import select_frame_by_name
from .functions.open_files import open_files_action
import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image
from .thread import ThreadCompresProcess
# customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("KOPIRI")
        self.geometry("770x800")
        self.resizable(False, False)

        self.files = []

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        image_path = os.path.join(os.path.dirname(
            os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(
            image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "title_image.png")), size=(500, 150))
        self.image_icon_image = customtkinter.CTkImage(Image.open(
            os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=" KOPIRI", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="WEB",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="CONFIGURACIÓN",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.chat_image, anchor="w", command=self.frame_2_button_event)
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

        # input file

        self.input_select_files = customtkinter.CTkButton(
            self.home_frame,
            text="Seleccionar imagenes",
            image=self.image_icon_image, compound="right",
            command=self.open_files,
            font=customtkinter.CTkFont(size=20, weight="bold")
        )

        # todo el ancho de la columna
        self.input_select_files.grid(
            row=1, column=0, padx=20, pady=10, sticky="ew")

        # create textbox
        self.text_frame = customtkinter.CTkFrame(
            self.home_frame, corner_radius=0, fg_color=("gray90", "gray10"), border_width=1, border_color="gray50")
        self.text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.label_upload = customtkinter.CTkLabel(
            self.text_frame, text="Archivos subidos (0)")
        self.label_upload.grid(row=0, column=0, padx=20, pady=5)

        self.label_supported = customtkinter.CTkLabel(
            self.text_frame, text="Archivos soportados (0)")
        self.label_supported.grid(row=1, column=0, padx=20, pady=5)

        self.textbox = customtkinter.CTkTextbox(self.text_frame, width=500)
        self.textbox.grid(row=2, column=0, padx=20, pady=10, sticky="nsew")

        # quality
        self.quality_frame = customtkinter.CTkFrame(
            self.home_frame, corner_radius=0, fg_color=("gray90", "gray10"), border_width=1, border_color="gray50")
        self.quality_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.label_quality = customtkinter.CTkLabel(
            self.quality_frame, text="Calidad (1-100)")
        self.label_quality.grid(row=0, column=0, padx=20, pady=5)

        self.sd_quality = customtkinter.CTkSlider(
            self.quality_frame, from_=1, to=100, number_of_steps=100, width=450)
        self.sd_quality.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        self.lb_quality = customtkinter.CTkLabel(
            self.quality_frame)
        self.lb_quality.grid(row=1, column=2, padx=20, pady=5)
        # optimize

        self.optimize_frame = customtkinter.CTkFrame(
            self.home_frame, corner_radius=0, fg_color=("gray90", "gray10"), border_width=1, border_color="gray50")
        self.optimize_frame.grid(
            row=4, column=0, padx=20, pady=10, sticky="ew")

        self.label_optimize = customtkinter.CTkLabel(
            self.optimize_frame, text="Peso KB")
        self.label_optimize.grid(row=0, column=0, padx=20, pady=5)

        self.sd_optimize = customtkinter.CTkSlider(
            self.optimize_frame, from_=1, to=700, number_of_steps=14, width=450)
        self.sd_optimize.grid(row=1, column=0, padx=20, pady=5, sticky="ew")
        self.lb_optimize = customtkinter.CTkLabel(
            self.optimize_frame)
        self.lb_optimize.grid(row=1, column=2, padx=20, pady=5, sticky="ew")

        # button compress
        self.compress_button = customtkinter.CTkButton(
            self.home_frame, text="Comprimir", image=self.image_icon_image, compound="right", command=self.compress,
            font=customtkinter.CTkFont(size=20, weight="bold")

        )
        self.compress_button.grid(
            row=5, column=0, padx=20, pady=10, sticky="ew")

        self.progress_bar = customtkinter.CTkProgressBar(
            self.home_frame)
        self.progress_bar.grid(
            row=6, column=0, padx=20, pady=10, sticky="ew")

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

        # hidden frame
        self.sd_quality.configure(command=self.update_quality)

        self.sd_optimize.configure(command=self.update_optimize)

        self.text_frame.grid_forget()
        self.quality_frame.grid_forget()
        self.optimize_frame.grid_forget()
        self.progress_bar.grid_forget()
        self.compress_button.grid_forget()

    def clear_config(self):
        self.output_frame_textbox.delete(0, tkinter.END)
        self.quality_config_frame_textbox.delete(0, tkinter.END)
        self.weight_config_frame_textbox.delete(0, tkinter.END)
        self.weight_max_config_frame_textbox.delete(0, tkinter.END)

    def read_config(self):
        config = Config()
        if config.get_manipulation() == False:
            config.set_output_dir(os.path.join(
                os.path.expanduser("~"), "Desktop", "kopiriApp", "app", "out"))
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

        self.sd_optimize.configure(
            from_=100, to=int(self.weight_max_config_frame_textbox.get()), number_of_steps=int(self.weight_max_config_frame_textbox.get()) / 10
        )

        self.sd_optimize.set(int(self.weight_config_frame_textbox.get()))
        self.lb_optimize.configure(text=str(
            self.weight_config_frame_textbox.get()))

    def open_files(self):
        open_files_action(self)

    def show_frames(self):
        self.text_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        self.quality_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        self.optimize_frame.grid(
            row=4, column=0, padx=20, pady=10, sticky="ew")

    def update_quality(self, event):
        value = self.sd_quality.get()
        value = int(value)
        self.lb_quality.configure(
            text=str(value))

    def update_optimize(self, event):
        value = self.sd_optimize.get()
        value = int(value)
        self.lb_optimize.configure(
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
        thread = ThreadCompresProcess(
            files=self.files, quality=int(self.sd_quality.get()), weight_max=int(self.sd_optimize.get()), progress_bar=self.progress_bar)
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


def init():
    app = App()
    app.mainloop()
