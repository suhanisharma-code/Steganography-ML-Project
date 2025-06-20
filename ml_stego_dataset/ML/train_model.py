import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import joblib
import os

# --- Step 1: Load Dataset Safely ---
current_folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_folder, "stego_features_dataset.csv")

print("📁 Looking for CSV at:", csv_path)

if not os.path.exists(csv_path):
    print("❌ CSV file not found. Please make sure 'stego_features_dataset.csv' is in the same folder.")
    exit()

df = pd.read_csv(csv_path)

# --- Step 2: Prepare Data ---
X = df.drop("label", axis=1)
y = df["label"]

# --- Step 3: Train-Test Split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --- Step 4: Train Random Forest ---
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)
print(f"🌲 Random Forest Accuracy: {rf_acc * 100:.2f}%")

# --- Step 5: Train SVM ---
svm_model = SVC(kernel="linear", probability=True)
svm_model.fit(X_train, y_train)
svm_pred = svm_model.predict(X_test)
svm_acc = accuracy_score(y_test, svm_pred)
print(f"🤖 SVM Accuracy: {svm_acc * 100:.2f}%")

# --- Step 6: Save Models ---
joblib.dump(rf_model, os.path.join(current_folder, "rf_model.pkl"))
joblib.dump(svm_model, os.path.join(current_folder, "svm_model.pkl"))
print("📦 Models saved as 'rf_model.pkl' and 'svm_model.pkl'")

# --- Step 7: Default Save (RF as final_model.pkl) ---
joblib.dump(rf_model, os.path.join(current_folder, "final_model.pkl"))
print("✅ Random Forest also saved as 'final_model.pkl'")