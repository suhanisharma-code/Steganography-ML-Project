import joblib
from PIL import Image
import numpy as np
import os

# --- Setup ---
current_folder = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_folder, "rf_model.pkl")
img_path = os.path.join(current_folder, "test_images", "clean_1.png")

# --- Load Model ---
if not os.path.exists(model_path):
    print("❌ Model file not found.")
    exit()
model = joblib.load(model_path)

# --- Feature Extraction with 9 Features ---
def extract_features(img_path):
    img = Image.open(img_path).resize((64, 64)).convert("RGB")
    arr = np.array(img)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]

    features = [
        np.mean(r),
        np.mean(g),
        np.mean(b),
        np.std(r),
        np.std(g),
        np.std(b),
        np.max(r) - np.min(r),
        np.max(g) - np.min(g),
        np.max(b) - np.min(b)
    ]
    return np.array(features).reshape(1, -1)

# --- Predict ---
if not os.path.exists(img_path):
    print(f"❌ Image not found: {img_path}")
    exit()

features = extract_features(img_path)
prediction = model.predict(features)[0]
label = "🔴 Encoded" if prediction == 1 else "🟢 Clean"

print(f"📌 Prediction for '{os.path.basename(img_path)}': {label}")