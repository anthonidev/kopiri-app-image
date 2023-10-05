from PIL import Image
import os


class CompressWeb():
    def __init__(self, files, quality, weight_max, output_dir, progress_bar, label_progress_bar, textbox):
        self.files = files
        self.quality = quality
        self.weight_max = weight_max * 1000
        self.output_dir = output_dir
        self.progress_bar = progress_bar
        self.label_progress_bar = label_progress_bar
        self.textbox = textbox

        self.weight_initial = 0
        self.weight_final = 0

        self.supported_files_list = ['.png', '.jpg', '.jpeg',  '.webp']

        self.compress()

    def compress(self):
        self.weight_initial = sum(os.stat(file).st_size for file in self.files if os.path.splitext(
            file)[1].lower() in self.supported_files_list)
        self.progress_bar.set(0)
        self.progress_bar.start()

        for index, file in enumerate(self.files):
            output_path, current_weight = self.compress_image(file)
            if output_path:
                self.weight_final += current_weight
                self.update_ui(index, os.path.basename(
                    output_path), current_weight)
        self.textbox.configure(state="normal")

        self.textbox.insert("end", f' \n \n')
        self.textbox.insert("end", f'{"-"*70} \n')
        self.textbox.insert("end", f'{"-"*70} \n')
        self.textbox.insert(
            "end", f'{"-"*10} Peso inicial: {self.weight_initial/1000} kb  \n', "bold")
        self.textbox.insert(
            "end", f'{"-"*10} Peso final: {self.weight_final/1000} kb  \n', "bold")
        self.textbox.insert("end", f'{"-"*70} \n')
        self.textbox.insert("end", f'{"-"*70} \n')
        self.textbox.insert("end", f' \n')
        self.textbox.insert("end", f' \n')
        self.textbox.insert(
            "end", f'Se ha reducido el peso en {round((1-(self.weight_final/self.weight_initial))*100)}% \n')

        self.textbox.configure(state="disabled")
        self.textbox.see("end")

        self.progress_bar.stop()

    def compress_image(self, file_path):
        name, extension = os.path.splitext(file_path)
        name = os.path.basename(name)

        if extension.lower() not in self.supported_files_list:
            return None, 0

        output_path = os.path.join(self.output_dir, name + ".webp")
        picture = Image.open(file_path).convert("RGB")

        picture.save(output_path, "webp", optimize=True, quality=self.quality)
        current_weight = os.stat(output_path).st_size
        new_quality = self.quality

        while current_weight > self.weight_max and new_quality > 10:  # Límite de calidad a 10
            new_quality -= 5
            picture.save(output_path, "webp",
                         optimize=True, quality=new_quality)
            current_weight = os.stat(output_path).st_size

        picture.close()
        return output_path, current_weight

    def update_ui(self, index, name, current_weight):
        line = f'{index+1}. ✅ {name} - {current_weight/1000} kb \n'
        self.textbox.configure(state="normal")
        self.textbox.insert("end", line)
        self.textbox.configure(state="disabled")
        self.textbox.see("end")

        progress = (index + 1) / len(self.files)
        self.progress_bar.set(progress)
        self.label_progress_bar.configure(
            text=str(round(progress * 100)) + "%")
