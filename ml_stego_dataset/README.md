#  Secure Steganography with GUI & Machine Learning Detection

A Python-based desktop application to hide secret messages inside images using *steganography, protected by a **password, and further enhanced with **ML detection* to verify if an image contains hidden data.

---

##  Features

-  *GUI-based* message encoding & decoding using Tkinter
-  *Password-protected* steganography
-  *Machine Learning Model* to detect if a message is hidden in an image (using Random Forest & SVM)
-  Dataset creation, auto image encoding, and feature extraction
-  Accuracy achieved: *~82%*
-  Simple & user-friendly design

---

##  How It Works

1. *Encode Message*
   - Enter a message and password.
   - Select an image (.png) → Hidden message saved with password.

2. *Decode Message*
   - Upload the encoded image.
   - Enter the correct password to retrieve the message.

3. *Detect Hidden Message (ML)*
   - Click a button, upload image.
   - ML model predicts whether the image is clean or encoded.

---

##  ML Details

- *Algorithms Used*:
  - Random Forest Classifier (Best Accuracy)
  -  Support Vector Machine (SVM)

- *Features Extracted*:
  - RGB Mean, Standard Deviation, Min/Max values

- *Dataset*:
  - Custom dataset created with:
    - 30+ clean images
    - 30+ encoded images (auto generated)

- *Accuracy Achieved*:
  -  RF: ~82%
  - SVM: ~48%

---

