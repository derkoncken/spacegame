from PIL import Image
import os

# ins Arbeitsverzeichnis wechseln (Ordner, in dem das Skript liegt)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def trim_transparent_border(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    alpha = img.split()[-1]

    bbox = alpha.getbbox()
    if bbox:
        trimmed = img.crop(bbox)
        trimmed.save(output_path)
        print(f"Bild erfolgreich gespeichert unter: {output_path}")
    else:
        print(f"{input_path}: Keine nicht-transparenten Pixel gefunden.")

if __name__ == "__main__":
    for filename in os.listdir("."):
        if filename.lower().endswith(".png"):
            input_path = filename
            # Ausgabedatei z. B. mit Suffix "_trimmed"
            name, ext = os.path.splitext(filename)
            trim_transparent_border(input_path, input_path)
