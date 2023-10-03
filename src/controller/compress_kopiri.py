from PIL import Image
import os
from utils.supported import supported_file_extensions


def compress_image(file_path, output_dir, quality=100, weight_max=300000):
    name, extension = os.path.splitext(file_path)
    name = os.path.basename(name)

    if extension.lower() not in supported_file_extensions:
        return None, 0

    output_path = os.path.join(output_dir, name + ".webp")
    picture = Image.open(file_path).convert("RGB")

    picture.save(output_path, "webp", optimize=True, quality=quality)
    current_weight = os.stat(output_path).st_size
    new_quality = quality

    while current_weight > weight_max and new_quality > 10:  # Límite de calidad a 10
        new_quality -= 5
        picture.save(output_path, "webp", optimize=True, quality=new_quality)
        current_weight = os.stat(output_path).st_size

    picture.close()
    return output_path, current_weight


def update_ui(progress_bar, label_progress_bar, textbox, index, name, current_weight, files):
    line = f'{index+1}. ✅ {name} - {current_weight/1000} kb \n'
    textbox.configure(state="normal")
    textbox.insert("end", line)
    textbox.configure(state="disabled")
    textbox.see("end")

    progress = (index + 1) / len(files)
    progress_bar.set(progress)
    label_progress_bar.configure(text=str(round(progress * 100)) + "%")


def compress_kopiri(
    files=[],
    quality=100,
    weight_max=300000,
    output_dir="C:/Users/Toni/Desktop/kopiriApp/app/out/",
    progress_bar=None,
    label_progress_bar=None,
    textbox=None
):
    weight_initial = sum(os.stat(file).st_size for file in files if os.path.splitext(
        file)[1].lower() in supported_file_extensions)
    weight_final = 0

    progress_bar.set(0)
    progress_bar.start()

    for index, file in enumerate(files):
        output_path, current_weight = compress_image(
            file, output_dir, quality, weight_max)
        if output_path:
            weight_final += current_weight
            update_ui(progress_bar, label_progress_bar, textbox, index,
                      os.path.basename(output_path), current_weight, files)

    textbox.configure(state="normal")

    textbox.insert("end", f' \n \n')
    textbox.insert("end", f'{"-"*70} \n')
    textbox.insert("end", f'{"-"*70} \n')
    textbox.insert(
        "end", f'{"-"*10} Peso inicial: {weight_initial/1000} kb  \n', "bold")
    textbox.insert(
        "end", f'{"-"*10} Peso final: {weight_final/1000} kb  \n', "bold")
    textbox.insert("end", f'{"-"*70} \n')
    textbox.insert("end", f'{"-"*70} \n')
    textbox.insert("end", f' \n')
    textbox.insert("end", f' \n')
    textbox.insert(
        "end", f'Se ha reducido el peso en {round((1-(weight_final/weight_initial))*100)}% \n')

    textbox.configure(state="disabled")
    textbox.see("end")

    progress_bar.stop()
