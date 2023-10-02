from customtkinter import filedialog
import tkinter
from utils.supported import supported_file_extensions


def open_files_action(self):
    uploaded_files_list = list(filedialog.askopenfilenames())
    uploaded_files_counter = len(uploaded_files_list)
    supported_files_list = check_supported_selected_files(
        uploaded_files_list)
    supported_files_counter = len(supported_files_list)

    if supported_files_counter > 0:
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        self.show_frames()
        text = "\n".join(supported_files_list)
        self.textbox.insert("0.0", text)
        self.textbox.configure(state="disabled")

        self.label_upload.configure(
            text="Archivos subidos (" + str(uploaded_files_counter) + ")")
        self.label_supported.configure(
            text="Archivos soportados (" + str(supported_files_counter) + ")")

        self.files = supported_files_list
        self.compress_button.grid(
            row=5, column=0, padx=20, pady=10, sticky="ew")

        tkinter.messagebox.showinfo(
            "Archivos", "Se han seleccionado " + str(supported_files_counter) + " archivos soportados")

    else:
        tkinter.messagebox.showerror("Archivos",
                                     "No se han seleccionado archivos soportados")


def check_supported_selected_files(uploaded_file_list):
    supported_files_list = []
    for file in uploaded_file_list:
        if any(file.endswith(supported_extension) for supported_extension in supported_file_extensions):
            supported_files_list.append(file)

    return supported_files_list
