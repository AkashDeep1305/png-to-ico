from PIL import Image
import os

def convert_png_to_ico(input_png_path, output_ico_path, sizes):
    """
    Convert a PNG image to an ICO format.

    :param input_png_path: Path to the input PNG file.
    :param output_ico_path: Path where the output ICO file will be saved.
    :param sizes: A list of icon sizes to include in the ICO file.
    """
    try:
        # Open the PNG file
        img = Image.open(input_png_path)

        # Ensure the image has an alpha channel (for transparency)
        img = img.convert("RGBA")

        # Save as ICO with specified sizes
        img.save(output_ico_path, format="ICO", sizes=sizes)
        print(f"ICO file created successfully at: {output_ico_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_png = input("Enter the path of the PNG file: ").strip().strip('"')
    output_dir = input("Enter the directory for the output ICO file: ").strip().strip('"')

    # Ask user for desired sizes
    print("Enter the icon sizes you want (e.g., 256x256, 128x128). Separate multiple sizes with commas:")
    sizes_input = input().strip()
    try:
        sizes = [tuple(map(int, size.strip().split('x'))) for size in sizes_input.split(',')]
    except ValueError:
        print("Invalid size format. Please use the format widthxheight (e.g., 256x256).")
        exit(1)

    # Generate output ICO file path
    output_ico = os.path.join(output_dir, os.path.splitext(os.path.basename(input_png))[0] + '.ico')
    convert_png_to_ico(input_png, output_ico, sizes)