import customtkinter


class Navigation:
    def __init__(self, master):
        self.master = master
        self.setup_ui()

    def setup_ui(self):
        self.navigation_frame = customtkinter.CTkFrame(
            self.master,
            corner_radius=0
        )
        self.navigation_frame.grid(
            row=0, column=0,
            sticky="nsew"
        )
        self.navigation_frame.grid_rowconfigure(
            4,
            weight=1
        )
        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame,
            text=" KOPIRI",
            image=self.master.logo_image,
            compound="left",
            font=customtkinter.CTkFont(size=15, weight="bold")
        )
        self.navigation_frame_label.grid(
            row=0, column=0,
            padx=20, pady=20
        )
        self.web_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="WEB",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.master.web_icon,
            anchor="w",
            command=self.web_button_event,
        )
        self.web_button.grid(row=1, column=0, sticky="ew")
        self.config_button = customtkinter.CTkButton(
            self.navigation_frame,
            corner_radius=0,
            height=40,
            border_spacing=10,
            text="CONFIGURACIÓN",
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            image=self.master.config_icon,
            anchor="w",
            command=self.config_button_event
        )
        self.config_button.grid(row=2, column=0, sticky="ew")
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame,
            values=["Dark", "Light", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_menu.grid(
            row=6, column=0,
            padx=20, pady=20,
            sticky="s"
        )
        self.frames()
        self.select_frame_by_name("web")

    def frames(self):
        self.master.web_frame = customtkinter.CTkFrame(
            self.master,
            corner_radius=0,
            fg_color="transparent"
        )
        self.master.web_frame.grid_columnconfigure(5, weight=1)
        self.master.config_frame = customtkinter.CTkFrame(
            self.master,
            corner_radius=0,
            fg_color="transparent"
        )

    def select_frame_by_name(self, name):
        self.web_button.configure(
            fg_color=("gray75", "gray25") if name == "web" else "transparent"
        )
        self.config_button.configure(
            fg_color=("gray75", "gray25") if name == "config" else "transparent"
        )

        if name == "web":
            self.master.web_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.master.web_frame.grid_forget()
        if name == "config":
            self.master.config_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.master.config_frame.grid_forget()

    def web_button_event(self):
        self.select_frame_by_name("web")

    def config_button_event(self):
        self.select_frame_by_name("config")

    def change_appearance_mode_event(self, new_appearance_mode):
        self.master.change_appearance_mode_event(new_appearance_mode)
