def select_frame_by_name(self, name):
    self.home_button.configure(
        fg_color=("gray75", "gray25") if name == "home" else "transparent")
    self.frame_2_button.configure(
        fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

    # show selected frame
    if name == "home":
        self.home_frame.grid(row=0, column=1, sticky="nsew")
    else:
        self.home_frame.grid_forget()
    if name == "frame_2":
        self.second_frame.grid(row=0, column=1, sticky="nsew")
    else:
        self.second_frame.grid_forget()
