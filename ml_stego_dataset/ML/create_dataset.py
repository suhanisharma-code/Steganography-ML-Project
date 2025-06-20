import os
import numpy as np
import pandas as pd
from PIL import Image

def extract_features(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((64, 64))  # resize to normalize size
    pixels = np.array(img)

    r_vals = pixels[:, :, 0].flatten()
    g_vals = pixels[:, :, 1].flatten()
    b_vals = pixels[:, :, 2].flatten()

    return [
        np.mean(r_vals),
        np.mean(g_vals),
        np.mean(b_vals),
        np.std(r_vals),
        np.std(g_vals),
        np.std(b_vals),
        np.max(r_vals) - np.min(r_vals),
        np.max(g_vals) - np.min(g_vals),
        np.max(b_vals) - np.min(b_vals)
    ]

data = []
labels = []

# Clean images → label 0
clean_path = "ml_stego_dataset/ML/clean"
for filename in os.listdir(clean_path):
    if filename.endswith(".png"):
        path = os.path.join(clean_path, filename)
        features = extract_features(path)
        data.append(features)
        labels.append(0)

# Encoded images → label 1
encoded_path = "ml_stego_dataset/ML/encoded"
for filename in os.listdir(encoded_path):
    if filename.endswith(".png"):
        path = os.path.join(encoded_path, filename)
        features = extract_features(path)
        data.append(features)
        labels.append(1)

# Combine into DataFrame
df = pd.DataFrame(data, columns=[
    "mean_r", "mean_g", "mean_b",
    "std_r", "std_g", "std_b",
    "range_r", "range_g", "range_b"
])
df["label"] = labels

# Save to CSV
df.to_csv("stego_features_dataset.csv", index=False)
print("✅ Dataset created and saved as stego_features_dataset.csv")