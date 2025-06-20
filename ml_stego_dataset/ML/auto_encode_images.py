import os
from PIL import Image
import random

# --- Encode Function ---
def encode_image(input_path, output_path, message):
    img = Image.open(input_path).convert("RGB")
    encoded = img.copy()
    width, height = img.size
    index = 0
    message += "$t3g0"

    for row in range(height):
        for col in range(width):
            if index < len(message):
                r, g, b = img.getpixel((col, row))
                encoded.putpixel((col, row), (r, g, ord(message[index])))
                index += 1
            else:
                break
        if index >= len(message):
            break

    encoded.save(output_path)

# --- Folders ---
current_folder = os.path.dirname(os.path.abspath(__file__))
clean_folder = os.path.join(current_folder, "clean")
encoded_folder = os.path.join(current_folder, "encoded")

# ✅ Check clean folder exists
if not os.path.exists(clean_folder):
    print(f"❌ 'clean/' folder not found at: {clean_folder}")
    print("📂 Please create the folder and add .png images inside it.")
    exit()

# ✅ Create encoded folder if not exists
if not os.path.exists(encoded_folder):
    os.makedirs(encoded_folder)

# --- Encode all clean images ---
for filename in os.listdir(clean_folder):
    if filename.lower().endswith(".png"):
        input_path = os.path.join(clean_folder, filename)
        output_path = os.path.join(encoded_folder, "encoded_" + filename)
        message = "THIS_IS_SECRET_" + str(random.randint(1000, 9999))

        try:
            encode_image(input_path, output_path, message)
            print(f"✅ Encoded: {filename}")
        except Exception as e:
            print(f"❌ Failed: {filename} → {e}")

print("🎉 Encoding complete!")