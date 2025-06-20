import os
import numpy as np
from PIL import Image

output_folder = "ml_stego_dataset/clean"
os.makedirs(output_folder, exist_ok=True)

for i in range(400):  # Generate 30 clean images
    data = np.random.randint(0, 256, (64, 64), dtype=np.uint8)
    img = Image.fromarray(data)
    img.save(os.path.join(output_folder, f"clean_{i}.png"))

print("✅ Clean images created.")