from rembg import remove, new_session
from PIL import Image
import os

input_dir = "images_RH2"
output_dir = "images_bg_RH2"

os.makedirs(output_dir, exist_ok=True)

session = new_session("birefnet-general")

for filename in os.listdir(input_dir):

    if filename.endswith(".png"):

        input_path = os.path.join(
            input_dir,
            filename
        )

        output_path = os.path.join(
            output_dir,
            filename.replace(".png", ".png")
        )

        print("processing:", filename)

        img = Image.open(input_path)

        result = remove(
            img,
            session=session
        )

        result.save(output_path)

print("All finished!")