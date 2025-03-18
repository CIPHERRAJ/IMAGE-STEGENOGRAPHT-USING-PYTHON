Image Steganography Application

Overview:

This is a Python-based Image Steganography Application built using Tkinter for GUI and OpenCV for image processing. It allows users to securely hide messages within images using the Least Significant Bit (LSB) technique and later retrieve them using a password.

Features:

Modern GUI with stylish buttons and entry fields
Image Selection to choose an image for encryption or decryption
Message Encryption: Hide a secret message inside an image
Message Decryption: Extract the hidden message from an encrypted image
Password Protection: Ensures secure access to the hidden message
Error Handling: Provides alerts for invalid operations

Technologies Used:
Python (Programming Language)
Tkinter (Graphical User Interface)
OpenCV (Image Processing)
PIL (Pillow) (Image Handling)
NumPy (Array Manipulation)
Installation

Prerequisites:
Ensure you have Python 3.x installed. You also need to install the required dependencies:
pip install opencv-python numpy pillow

How to Run?
Clone or download this repository.
Navigate to the project directory.

Run the following command:
python steganography.py
The GUI window will open.

Usage:
1. Select an Image
Click Select Image to choose an image.
The image will be displayed in the application.

2. Encrypt a Message
Click Encrypt Message.
Enter the secret message and a password.
Click Encrypt & Save to hide the message inside the image.

3. Decrypt a Message
Click Decrypt Message.
Enter the correct password.
The hidden message will be displayed.

File Structure:

├── steganography.py      # Main application script
├── encrypted_image.png   # Encrypted output image
├── README.md             # Documentation

Limitations:
The image size should be large enough to store the message.
If the password is incorrect, decryption will be denied.

License:
This project is open-source and free to use under the MIT License.
