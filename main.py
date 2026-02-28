import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os
import sys

def normalize_txt_path(name):
    name = name.strip()
    if not name.lower().endswith(".txt"):
        name += ".txt"
    return name

def normalize_png_path(name):
    name = name.strip()
    if not name.lower().endswith(".png"):
        name += ".png"
    return name

def file_exists(path):
    return os.path.isfile(path)

def load_font(font_path, size):
    try:
        return ImageFont.truetype(font_path, size)
    except Exception:
        print("Custom font not found. Falling back to default font.")
        return ImageFont.load_default()

def ascii_to_png_highres(
    txt_path,
    output_path,
    font_path="C:/Windows/Fonts/consola.ttf",
    target_width=3840
):
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if not lines or all(line.strip() == "" for line in lines):
        print("TXT file is empty or invalid.")
        return

    max_line_length = max(len(line) for line in lines)
    base_font_size = 12
    padding = 40

    font = load_font(font_path, base_font_size)
    char_width = font.getlength("A")

    estimated_width = char_width * max_line_length + padding * 2
    scale_factor = target_width / max(estimated_width, 1)
    new_font_size = max(1, int(base_font_size * scale_factor))

    font = load_font(font_path, new_font_size)
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

    print("✔ 4K PNG generated successfully.")
    print(f"Saved → {output_path}")

def main():
    while True:
        print("\n====================================")
        print("ASCII TXT → 4K PNG RENDERER")
        print("Type 'quit' anytime to exit.")
        print("====================================\n")

        txt_input = input("Enter ASCII file name: ").strip()

        if txt_input.lower() in ["quit", "exit"]:
            print("Exiting.")
            sys.exit(0)

        txt_path = normalize_txt_path(txt_input)

        if not file_exists(txt_path):
            print(f"File not found: {txt_path}")
            continue

        output_input = input("Enter output PNG name: ").strip()

        if output_input.lower() in ["quit", "exit"]:
            print("Exiting.")
            sys.exit(0)

        output_path = normalize_png_path(output_input)

        ascii_to_png_highres(txt_path, output_path)

if __name__ == "__main__":
    main()