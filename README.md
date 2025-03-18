# Image Steganography Application

## Overview
This is a Python-based Image Steganography Application built using Tkinter for GUI and OpenCV for image processing. It allows users to securely hide messages within images using the Least Significant Bit (LSB) technique and later retrieve them using a password.

## Features
- **Modern GUI** with stylish buttons and entry fields
- **Image Selection** to choose an image for encryption or decryption
- **Message Encryption**: Hide a secret message inside an image
- **Message Decryption**: Extract the hidden message from an encrypted image
- **Password Protection**: Ensures secure access to the hidden message
- **Error Handling**: Provides alerts for invalid operations

## Technologies Used
- **Python** (Programming Language)
- **Tkinter** (Graphical User Interface)
- **OpenCV** (Image Processing)
- **PIL (Pillow)** (Image Handling)
- **NumPy** (Array Manipulation)

## Installation

### Prerequisites
Ensure you have Python 3.x installed. You also need to install the required dependencies:
```bash
pip install opencv-python numpy pillow
```

### How to Run
1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the following command:
   ```bash
   python steganography.py
   ```
4. The GUI window will open.

## Usage

### Select an Image
1. Click **Select Image** to choose an image.
2. The image will be displayed in the application.

### Encrypt a Message
1. Click **Encrypt Message**.
2. Enter the secret message and a password.
3. Click **Encrypt & Save** to hide the message inside the image.

### Decrypt a Message
1. Click **Decrypt Message**.
2. Enter the correct password.
3. The hidden message will be displayed.

## File Structure
```
├── steganography.py     # Main application script
├── encrypted_image.png  # Encrypted output image
├── README.md            # Documentation
```

## Limitations
- The image size should be large enough to store the message.
- If the password is incorrect, decryption will be denied.

## License
This project is open-source and free to use under the **MIT License**.
