import customtkinter
from tkinter import filedialog, messagebox
from src.controller.config_actions import ConfigActions
import os


class ConfigFrame():
    def __init__(self, master):
        self.master = master
        self.config_frame = master.config_frame
        self.setup_ui()
        self.config = ConfigActions()
        self.read_config()

    def setup_ui(self):
        self.output_frame_ui()
        self.quality_frame_ui()
        self.weight_frame_ui()
        self.action_button_ui()
        pass

    def output_frame_ui(self):
        self.banner = customtkinter.CTkLabel(
            self.config_frame, text="", image=self.master.banner_image_config)

        self.banner.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.output_frame = customtkinter.CTkFrame(
            self.config_frame,
            corner_radius=0,
            fg_color=("gray90", "gray10")
        )
        self.output_frame.grid(
            row=1, column=0,
            padx=20, pady=10,
            sticky="ew"
        )
        self.output_frame.grid_rowconfigure(0, weight=1)
        self.output_frame.grid_columnconfigure(0, weight=1)

        self.output_frame_label = customtkinter.CTkLabel(
            self.output_frame,
            text="Ruta donde se guardaran los archivos"
        )
        self.output_frame_label.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.master.output_frame_textbox = customtkinter.CTkEntry(
            self.output_frame,
            width=500
        )
        self.output_frame_textbox = self.master.output_frame_textbox
        self.output_frame_textbox.grid(
            row=1, column=0,
            padx=20, pady=10,
            sticky="nsew"
        )

        self.output_frame_button = customtkinter.CTkButton(
            self.output_frame,
            text="Seleccionar carpeta",
            command=self.select_dir
        )
        self.output_frame_button.grid(
            row=2,
            column=0,
            padx=20,
            pady=10,
            sticky="ew"
        )

    def quality_frame_ui(self):
        self.quality_config_frame = customtkinter.CTkFrame(
            self.config_frame,
            corner_radius=0,
            fg_color=("gray90", "gray10")
        )
        self.quality_config_frame.grid(
            row=2, column=0,
            padx=20, pady=10,
            sticky="ew"
        )
        self.quality_config_frame.grid_rowconfigure(0, weight=1)
        self.quality_config_frame.grid_columnconfigure(1, weight=1)

        self.quality_config_frame_label = customtkinter.CTkLabel(
            self.quality_config_frame,
            text="Calidad por defecto",
            width=100
        )
        self.quality_config_frame_label.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.quality_config_frame_textbox = customtkinter.CTkEntry(
            self.quality_config_frame,
            width=300
        )
        self.quality_config_frame_textbox.grid(
            row=0, column=1,
            padx=20, pady=10,
            sticky="nsew"
        )

    def weight_frame_ui(self):
        self.weight_config_frame = customtkinter.CTkFrame(
            self.config_frame,
            corner_radius=0,
            fg_color=("gray90", "gray10")
        )
        self.weight_config_frame.grid(
            row=3, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.weight_config_frame_label = customtkinter.CTkLabel(
            self.weight_config_frame,
            text="Peso por defecto (KB)",
            width=100
        )
        self.weight_config_frame_label.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.weight_config_frame_textbox = customtkinter.CTkEntry(
            self.weight_config_frame,
            width=300
        )
        self.weight_config_frame_textbox.grid(
            row=0, column=1,
            padx=20, pady=10,
            sticky="nsew"
        )

        self.weight_max_config_frame_label = customtkinter.CTkLabel(
            self.weight_config_frame,
            text="Peso maximo por defecto (KB)",
            width=100
        )
        self.weight_max_config_frame_label.grid(
            row=1, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.weight_max_config_frame_textbox = customtkinter.CTkEntry(
            self.weight_config_frame,
            width=300
        )
        self.weight_max_config_frame_textbox.grid(
            row=1, column=1,
            padx=20, pady=10,
            sticky="nsew"
        )

    def action_button_ui(self):
        self.save_config_frame = customtkinter.CTkFrame(
            self.config_frame,
            corner_radius=0,
            fg_color="transparent"
        )

        self.save_config_frame.grid(
            row=4, column=0,
            padx=20, pady=10,
            sticky="ew"
        )
        self.save_config_frame.grid_rowconfigure(0, weight=1)
        self.save_config_frame.grid_columnconfigure(1, weight=1)

        self.button_default_config = customtkinter.CTkButton(
            self.save_config_frame,
            text="Restablecer",
            command=self.default_config
        )
        self.button_default_config.grid(
            row=0, column=0,
            padx=20, pady=10,
            sticky="ew"
        )

        self.button_save_config = customtkinter.CTkButton(
            self.save_config_frame,
            text="Guardar configuración",
            command=self.save_config
        )
        self.button_save_config.grid(
            row=0, column=1,
            padx=20, pady=10,
            sticky="ew"
        )

    def select_dir(self):
        output_dir = filedialog.askdirectory()
        if output_dir != "":
            self.output_frame_textbox.delete(0, customtkinter.END)
            self.output_frame_textbox.insert(0, output_dir + "/")
        else:
            pass

    def read_config(self):
        self.clear_config()
        self.config.set_init_app()

        self.output_frame_textbox.insert(
            0, self.config.get_config_value("output_dir")
        )

        self.quality_config_frame_textbox.insert(
            0, self.config.get_config_value("quality")
        )

        self.weight_config_frame_textbox.insert(
            0, self.config.get_config_value("weight")
        )
        self.weight_max_config_frame_textbox.insert(
            0, self.config.get_config_value("weight_max")
        )

        self.master.change_appearance_mode_event(
            self.config.get_config_value("theme")
        )

        self.apply_config()

    def clear_config(self):
        self.output_frame_textbox.delete(0, customtkinter.END)
        self.quality_config_frame_textbox.delete(0, customtkinter.END)
        self.weight_config_frame_textbox.delete(0, customtkinter.END)
        self.weight_max_config_frame_textbox.delete(0, customtkinter.END)

    def default_config(self):
        self.config.default_config()
        self.read_config()
        messagebox.showinfo(
            "Información",
            "Configuración restablecida correctamente"
        )

    def save_config(self):
        self.config.save_config(
            self.output_frame_textbox.get(),
            self.quality_config_frame_textbox.get(),
            self.weight_config_frame_textbox.get(),
            self.weight_max_config_frame_textbox.get()
        )
        self.read_config()
        messagebox.showinfo(
            "Información",
            "Configuración guardada correctamente"
        )

    def apply_config(self):
        self.master.sd_quality.set(
            int(self.quality_config_frame_textbox.get())
        )
        self.master.lb_quality.configure(text=str(
            self.quality_config_frame_textbox.get())
        )

        self.master.sd_weight.configure(
            from_=100,
            to=int(self.weight_max_config_frame_textbox.get()),
            number_of_steps=int(
                self.weight_max_config_frame_textbox.get()) / 10
        )

        self.master.sd_weight.set(int(self.weight_config_frame_textbox.get()))
        self.master.lb_weight.configure(
            text=str(self.weight_config_frame_textbox.get())
        )
