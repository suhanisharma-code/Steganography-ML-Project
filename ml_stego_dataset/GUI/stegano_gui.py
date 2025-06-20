from tkinter import *
from tkinter import filedialog, messagebox, simpledialog
from PIL import Image
import numpy as np
import joblib
import os

# --- Feature extractor for ML ---
def extract_features(img_path):
    img = Image.open(img_path).resize((64, 64)).convert("RGB")
    arr = np.array(img)
    r, g, b = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2]
    return [
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

# --- Encode message with password ---

def encode_message():
    message = text_entry.get("1.0", END).strip()
    password = password_entry.get().strip()

    if len(message) == 0:
        messagebox.showwarning("Empty Message", "⚠ Please enter a message to encode.")
        return
    if len(password) == 0:
        messagebox.showwarning("Empty Password", "⚠ Please enter a password.")
        return

    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    full_message = f"{password}::{message}$t3g0"  # Add password + end marker

    try:
        img = Image.open(file_path).convert("RGB")  # Force RGB mode
        width, height = img.size

        if len(full_message) > width * height:
            messagebox.showerror("Too Long", "❌ Message is too long for the selected image.")
            return

        encoded = img.copy()
        index = 0

        for row in range(height):
            for col in range(width):
                if index < len(full_message):
                    r, g, b = img.getpixel((col, row))
                    asc = ord(full_message[index])
                    encoded.putpixel((col, row), (r, g, asc))
                    index += 1
                else:
                    break
            if index >= len(full_message):
                break

        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            print("Saving to:", save_path)
            encoded.save(save_path)
            messagebox.showinfo("Success", "✅ Message encoded and image saved successfully!")
        else:
            print("❌ No save path selected.")

    except Exception as e:
        messagebox.showerror("Error", f"❌ Encoding failed: {str(e)}")

# --- Decode message with password check ---
def decode_message():
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    decode_password = simpledialog.askstring("Password Required", "Enter the password to decode:", show="*")
    if not decode_password:
        return

    img = Image.open(file_path).convert("RGB")
    width, height = img.size
    hidden_msg = ""

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            char = chr(b)
            hidden_msg += char
            if hidden_msg.endswith("$t3g0"):
                break
        else:
            continue
        break

    if "::" in hidden_msg:
        saved_password, secret_message = hidden_msg[:-5].split("::", 1)
        if decode_password != saved_password:
            messagebox.showerror("Incorrect Password", "❌ The password you entered is incorrect.")
            return
        result_box.delete("1.0", END)
        result_box.insert(END, secret_message)
    else:
        messagebox.showerror("Error", "❌ Invalid encoded image or message format.")

# --- ML Detection Function ---
def detect_hidden_message():
    file_path = filedialog.askopenfilename(title="Select Image for ML Detection", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return

    try:
        current_folder = os.path.dirname(os.path.abspath(__file__))
        model_path = os.path.join(current_folder, "final_model.pkl")
        if not os.path.exists(model_path):
            messagebox.showerror("Model Not Found", "❌ final_model.pkl not found in the directory.")
            return

        model = joblib.load(model_path)
        features = extract_features(file_path)
        prediction = model.predict([features])[0]
        result = "🔒 Hidden Message Detected (Encoded)" if prediction == 1 else "✅ No Hidden Message (Clean)"
        result_box.delete("1.0", END)
        result_box.insert(END, result)
        messagebox.showinfo("ML Prediction", result)

    except Exception as e:
        messagebox.showerror("Error", f"❌ Prediction Failed: {str(e)}")

# --- GUI Setup ---
root = Tk()
root.title("Secure Message Hider (with Password & ML Detection)")
root.geometry("460x500")
root.config(bg="#e6f2ff")

Label(root, text="Enter message to hide:", bg="#e6f2ff", font=("Arial", 12)).pack(pady=(10, 0))
text_entry = Text(root, height=4, width=45)
text_entry.pack()

Label(root, text="Enter password:", bg="#e6f2ff", font=("Arial", 12)).pack(pady=(10, 0))
password_entry = Entry(root, show="*", width=45)
password_entry.pack()

Button(root, text="Encode Message", command=encode_message, bg="#4CAF50", fg="white", width=30).pack(pady=10)
Button(root, text="Decode Message", command=decode_message, bg="#2196F3", fg="white", width=30).pack(pady=10)
Button(root, text="Detect Hidden Message (ML)", command=detect_hidden_message, bg="#9C27B0", fg="white", width=30).pack(pady=10)

Label(root, text="Result:", bg="#e6f2ff", font=("Arial", 12)).pack(pady=(15, 0))
result_box = Text(root, height=4, width=45)
result_box.pack()

root.mainloop()