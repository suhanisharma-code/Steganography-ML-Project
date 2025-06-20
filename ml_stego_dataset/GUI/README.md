# Steganography & ML-based Detection

This is a desktop GUI application built with Python and Tkinter. It hides messages inside images using steganography and detects encoded images using a trained ML model (Random Forest / SVM).

##  Features
- Encode message into PNG image with password
- Decode message using password
- ML model detects if an image contains a hidden message
- GUI using Tkinter

##  Tech Stack
- Python
- PIL (Pillow)
- Tkinter
- Scikit-learn
- NumPy
- Joblib

##  How to Run
1. Clone the repo
2. Install dependencies: pip install -r requirements.txt
3. Run: python stegano_gui.py

## ML Model
Trained on custom dataset of clean & encoded images using color-based features.