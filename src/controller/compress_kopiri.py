from PIL import Image
import os


def compress_kopiri(files, quality=100, weight_max=300000, output_dir="C:/Users/Toni/Desktop/kopiriApp/app/out/"):
    print("Compressing Kopiri")

    weight_initial = 0
    weight_final = 0

    supported_extensions = ['.png', '.jpg', '.jpeg',  '.svg']

    for file in files:
        name, extension = os.path.splitext(file)
        name = os.path.basename(name)

        if extension.lower() in supported_extensions:
            weight_initial += os.stat(file).st_size

            # Convertir todas las imágenes a .webp para la compresión
            name = name + ".webp"

            picture = Image.open(file).convert("RGB")
            picture.save(output_dir + name, "webp",
                         optimize=True, quality=quality)

            current_weight = os.stat(output_dir + name).st_size
            new_quality = quality

            while current_weight > weight_max:
                new_quality -= 5
                picture.save(output_dir + name, "webp",
                             optimize=True, quality=new_quality)
                current_weight = os.stat(output_dir + name).st_size

            weight_final += current_weight
            picture.close()

    print("Initial weight: ", weight_initial)
    print("Final weight: ", weight_final)
