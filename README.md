# ASCII TXT → 4K PNG Renderer

## Purpose

Many online ASCII converters (e.g. asciiart.eu) offer PNG export.  
However, dark-background ASCII art often suffers from:

- Washed-out contrast
- Poor gamma handling
- Inconsistent font spacing
- Low effective resolution

This tool fixes that.

It takes a `.txt` ASCII file and renders a **true 4K PNG** with:

- Solid black background
- High-resolution scaling
- Proper monospace font rendering
- 300 DPI output

Designed for wallpapers, portfolio use, or high-quality exports.

---

## How It Works

1. Reads ASCII text file
2. Calculates maximum line width
3. Dynamically scales font to hit target width (default 3840px)
4. Renders text onto a black canvas
5. Exports a 4K PNG

---

## Requirements

- Python 3.9+
- Pillow
- NumPy

Install dependencies:

```bash
pip install pillow numpy