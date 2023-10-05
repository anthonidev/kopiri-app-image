from tkinter import filedialog, messagebox


class OpenFilesAction():
    def __init__(self):
        self.files = []
        self.uploaded_file_list = []
        self.supported_files_list = []
        self.supported_file_extensions = ['.png', '.jpg', '.jpeg',  '.webp']
        self.response = False
        self.open_files()

    def open_files(self):
        self.uploaded_file_list = list(filedialog.askopenfilenames())
        self.supported_files_list = self.supported_files()
        self.message_box()

    def suploaded_files_counter(self):
        return len(self.uploaded_file_list)

    def supported_files_counter(self):
        return len(self.supported_files_list)

    def supported_files(self):
        supported_files_list = []
        if self.suploaded_files_counter() == 0:
            return supported_files_list
        for file in self.uploaded_file_list:
            if any(file.endswith(supported_extension) for supported_extension in self.supported_file_extensions):
                supported_files_list.append(file)

        return supported_files_list

    def message_box(self):
        if self.suploaded_files_counter() == 0:
            messagebox.showerror(
                "Error",
                "No se han seleccionado archivos"
            )
            self.response = False
        elif self.supported_files_counter() == 0:
            messagebox.showerror(
                "Error",
                "No se han seleccionado archivos soportados"
            )
            self.response = False
        else:
            messagebox.showinfo(
                "Información",
                "Se han seleccionado {} archivos, de los cuales {} son soportados".format(
                    self.suploaded_files_counter(),
                    self.supported_files_counter()
                )
            )
            self.response = True
