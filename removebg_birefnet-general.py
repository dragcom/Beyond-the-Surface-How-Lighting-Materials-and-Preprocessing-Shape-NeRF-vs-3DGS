import os
import argparse
from rembg import remove, new_session
from PIL import Image

def main():
    parser = argparse.ArgumentParser(description="Remove background from images using rembg.")
    parser.add_argument("-i", "--input", default="input", help="Input folder path")
    parser.add_argument("-o", "--output", default="output", help="Output folder path")
    parser.add_argument("-m", "--model", default="birefnet-general", help="Model name for rembg")
    args = parser.parse_args()

    input_dir = args.input
    output_dir = args.output
    model_name = args.model

    os.makedirs(output_dir, exist_ok=True)

    session = new_session(model_name)

    valid_extensions = (".png", ".jpg", ".jpeg", ".webp", ".bmp")

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(valid_extensions):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)

            print(f"Processing: {filename}")

            try:
                img = Image.open(input_path)
                result = remove(img, session=session)
                result.save(output_path)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    print("All finished!")

if __name__ == "__main__":
    main()
