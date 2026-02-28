import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

def ensure_extension(path, extension):
    if not path.lower().endswith(extension):
        return path + extension
    return path


def validate_file(path, label):
    if not os.path.exists(path):
        print(f"{label} not found: {path}")
        return False
    return True

def ascii_to_png_highres(
    txt_path,
    output_path,
    font_path="C:/Windows/Fonts/consola.ttf",
    target_width=3840 #4k
):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    max_line_length = max(len(line) for line in lines)
    base_font_size = 12
    padding = 40

    font = ImageFont.truetype(font_path, base_font_size)
    char_width = font.getlength("A")

    estimated_width = char_width * max_line_length + padding * 2
    scale_factor = target_width / estimated_width
    new_font_size = max(1, int(base_font_size * scale_factor))

    font = ImageFont.truetype(font_path, new_font_size)
    char_width = font.getlength("A")
    ascent, descent = font.getmetrics()
    char_height = ascent + descent

    img_width = int(char_width * max_line_length) + padding * 2
    img_height = int(char_height * len(lines)) + padding * 2

    image = Image.new("RGB", (img_width, img_height), "black")
    draw = ImageDraw.Draw(image)

    y = padding
    for line in lines:
        draw.text((padding, y), line, font=font, fill="white")
        y += char_height

    image.save(output_path, dpi=(300, 300))

    print("4K PNG generated.")
    print(f"Saved: {output_path}")

def main():
    while True:
        print("###############################################")
        print("#        ASCII TXT TO 4k PNG                  #")
        print("###############################################\n\n")

        txt_path = input("Enter ascii.txt's path: ").strip()
        if not validate_file(txt_path, "TXT file"):
            continue

        output_png = ensure_extension(
            input("Enter output PNG name: ").strip(), ".png"
        )

        ascii_to_png_highres(
            txt_path,
            output_png
        )

if __name__ == "__main__":
    main()