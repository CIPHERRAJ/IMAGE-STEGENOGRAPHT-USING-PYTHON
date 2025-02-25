import cv2
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk

class ModernButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            bg="#4a90e2",  # Modern blue
            fg="white",
            font=("Helvetica", 10, "bold"),
            relief="flat",
            borderwidth=0,
            padx=20,
            pady=8,
            cursor="hand2"  # Hand cursor on hover
        )
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.config(bg="#357abd")  # Darker blue on hover

    def on_leave(self, e):
        self.config(bg="#4a90e2")  # Original blue

class ModernEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            font=("Helvetica", 11),
            relief="flat",
            bg="white",
            insertbackground="#2f3542",  # Cursor color
            highlightthickness=1,
            highlightbackground="#dcdde1",
            highlightcolor="#4a90e2"
        )

class SteganographyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Steganography")
        self.root.geometry("600x700")
        
        # Set theme colors
        self.colors = {
            "primary": "#4a90e2",    # Modern blue
            "bg": "#f5f6fa",         # Light background
            "text": "#2f3542",       # Dark text
            "accent": "#ff6b81"      # Accent color
        }
        
        # Configure root window
        self.root.configure(bg=self.colors["bg"])
        
        self.selected_image = None
        self.password = ""
        
        # Create container for all frames
        self.container = tk.Frame(root, bg=self.colors["bg"])
        self.container.pack(side="top", fill="both", expand=True)
        
        # Dictionary to store frames
        self.frames = {}
        
        # Create frames
        for F in (SelectionPage, EncryptionPage, DecryptionPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            frame.configure(bg=self.colors["bg"])
        
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.show_frame(SelectionPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def set_image(self, image_path):
        self.selected_image = image_path
    
    def get_image(self):
        return self.selected_image
    
    def set_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password

class SelectionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=controller.colors["bg"])
        
        # Create main container frame with padding
        main_frame = tk.Frame(self, bg=controller.colors["bg"])
        main_frame.pack(expand=True, padx=40, pady=20)
        
        # Decorative header
        header_frame = tk.Frame(main_frame, bg=controller.colors["primary"])
        header_frame.pack(fill="x", pady=(0, 20))
        
        label = tk.Label(header_frame, 
                        text="Image Steganography",
                        font=("Helvetica", 24, "bold"),
                        fg="white",
                        bg=controller.colors["primary"],
                        pady=20)
        label.pack()
        
        # Image selection area with border
        image_frame = tk.Frame(main_frame, 
                             bg="white",
                             highlightbackground=controller.colors["primary"],
                             highlightthickness=2)
        image_frame.pack(pady=20, padx=20)
        
        # Image display label with placeholder
        self.lbl_image = tk.Label(image_frame, 
                                 text="No image selected",
                                 font=("Helvetica", 12),
                                 bg="white",
                                 width=30,
                                 height=15)
        self.lbl_image.pack(padx=20, pady=20)
        
        # Button frame
        btn_frame = tk.Frame(main_frame, bg=controller.colors["bg"])
        btn_frame.pack(pady=20)
        
        # Image selection buttons
        self.btn_select = ModernButton(btn_frame,
                                     text="Select Image",
                                     command=self.select_image)
        self.btn_select.pack(pady=5)
        
        self.btn_clear = ModernButton(btn_frame,
                                    text="Clear Image",
                                    command=self.clear_image,
                                    state="disabled")
        self.btn_clear.pack(pady=5)
        
        # Separator
        ttk.Separator(main_frame, orient="horizontal").pack(fill="x", pady=20)
        
        # Operation buttons frame
        op_frame = tk.Frame(main_frame, bg=controller.colors["bg"])
        op_frame.pack(pady=10)
        
        self.btn_encrypt = ModernButton(op_frame,
                                      text="Encrypt Message",
                                      command=lambda: controller.show_frame(EncryptionPage),
                                      state="disabled")
        self.btn_encrypt.pack(pady=5)
        
        self.btn_decrypt = ModernButton(op_frame,
                                      text="Decrypt Message",
                                      command=lambda: controller.show_frame(DecryptionPage),
                                      state="disabled")
        self.btn_decrypt.pack(pady=5)
    
    def select_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.controller.set_image(file_path)
            self.load_image(file_path)
            self.btn_encrypt.config(state="normal")
            self.btn_decrypt.config(state="normal")
            self.btn_clear.config(state="normal")
    
    def clear_image(self):
        self.controller.set_image(None)
        self.lbl_image.config(image='')
        self.lbl_image.image = None
        self.lbl_image.config(text="No image selected")
        self.btn_encrypt.config(state="disabled")
        self.btn_decrypt.config(state="disabled")
        self.btn_clear.config(state="disabled")
    
    def load_image(self, image_path):
        img = Image.open(image_path)
        # Calculate aspect ratio
        aspect_ratio = img.width / img.height
        new_width = 300
        new_height = int(new_width / aspect_ratio)
        img = img.resize((new_width, new_height))
        img = ImageTk.PhotoImage(img)
        self.lbl_image.config(image=img, text="")
        self.lbl_image.image = img

class EncryptionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=controller.colors["bg"])
        
        main_frame = tk.Frame(self, bg=controller.colors["bg"])
        main_frame.pack(expand=True, padx=40, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=controller.colors["primary"])
        header_frame.pack(fill="x", pady=(0, 20))
        
        label = tk.Label(header_frame,
                        text="Encrypt Message",
                        font=("Helvetica", 20, "bold"),
                        fg="white",
                        bg=controller.colors["primary"],
                        pady=15)
        label.pack()
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg="white", padx=30, pady=30)
        content_frame.pack(fill="x")
        
        # Message entry
        tk.Label(content_frame,
                text="Enter Secret Message:",
                font=("Helvetica", 11, "bold"),
                bg="white").pack()
        self.entry_message = ModernEntry(content_frame, width=40)
        self.entry_message.pack(pady=(5, 15))
        
        # Password entry
        tk.Label(content_frame,
                text="Enter Password:",
                font=("Helvetica", 11, "bold"),
                bg="white").pack()
        self.entry_password = ModernEntry(content_frame, width=40, show="•")
        self.entry_password.pack(pady=5)
        
        # Button frame
        btn_frame = tk.Frame(main_frame, bg=controller.colors["bg"])
        btn_frame.pack(pady=20)
        
        ModernButton(btn_frame,
                    text="Encrypt & Save",
                    command=self.encrypt_message).pack(pady=5)
        ModernButton(btn_frame,
                    text="Back",
                    command=lambda: controller.show_frame(SelectionPage)).pack(pady=5)
    
    def encrypt_message(self):
        if not self.controller.get_image():
            messagebox.showerror("Error", "Please select an image first!")
            return
        
        message = self.entry_message.get()
        password = self.entry_password.get()
        
        if not message or not password:
            messagebox.showerror("Error", "Message and password cannot be empty!")
            return
        
        self.controller.set_password(password)
        
        try:
            img = cv2.imread(self.controller.get_image())
            
            message_length = len(message)
            message = f"{message_length:03d}" + message
            ascii_values = [ord(char) for char in message]
            
            required_pixels = len(ascii_values)
            total_pixels = img.shape[0] * img.shape[1] * 3
            
            if required_pixels > total_pixels:
                messagebox.showerror("Error", "Image is too small to store the message!")
                return
            
            index = 0
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    for k in range(3):
                        if index < len(ascii_values):
                            img[i, j, k] = ascii_values[index]
                            index += 1
                        else:
                            break
                    if index >= len(ascii_values):
                        break
                if index >= len(ascii_values):
                    break
            
            encrypted_path = "encrypted_image.png"
            cv2.imwrite(encrypted_path, img)
            
            messagebox.showinfo("Success", "Message encrypted successfully!")
            os.system(f'start "" "{encrypted_path}"')
            
            self.entry_message.delete(0, tk.END)
            self.entry_password.delete(0, tk.END)
            self.controller.show_frame(SelectionPage)
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

class DecryptionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(bg=controller.colors["bg"])
        
        main_frame = tk.Frame(self, bg=controller.colors["bg"])
        main_frame.pack(expand=True, padx=40, pady=20)
        
        # Header
        header_frame = tk.Frame(main_frame, bg=controller.colors["primary"])
        header_frame.pack(fill="x", pady=(0, 20))
        
        label = tk.Label(header_frame,
                        text="Decrypt Message",
                        font=("Helvetica", 20, "bold"),
                        fg="white",
                        bg=controller.colors["primary"],
                        pady=15)
        label.pack()
        
        # Content frame
        content_frame = tk.Frame(main_frame, bg="white", padx=30, pady=30)
        content_frame.pack(fill="x")
        
        # Password entry
        tk.Label(content_frame,
                text="Enter Password:",
                font=("Helvetica", 11, "bold"),
                bg="white").pack()
        self.entry_password = ModernEntry(content_frame, width=40, show="•")
        self.entry_password.pack(pady=5)
        
        # Button frame
        btn_frame = tk.Frame(main_frame, bg=controller.colors["bg"])
        btn_frame.pack(pady=20)
        
        ModernButton(btn_frame,
                    text="Decrypt",
                    command=self.decrypt_message).pack(pady=5)
        ModernButton(btn_frame,
                    text="Back",
                    command=lambda: controller.show_frame(SelectionPage)).pack(pady=5)
    
    def decrypt_message(self):
        if not self.controller.get_image():
            messagebox.showerror("Error", "Please select an image first!")
            return
        
        entered_password = self.entry_password.get()
        if entered_password != self.controller.get_password():
            messagebox.showerror("Error", "Incorrect password!")
            return
        
        try:
            img = cv2.imread(self.controller.get_image())
            if img is None:
                messagebox.showerror("Error", "Could not load image!")
                return
            
            ascii_values = []
            index = 0
            message_length = None
            
            for i in range(img.shape[0]):
                for j in range(img.shape[1]):
                    for k in range(3):
                        if index < 3:
                            ascii_values.append(img[i, j, k])
                            index += 1
                            if index == 3:
                                try:
                                    message_length = int("".join(map(chr, ascii_values)))
                                except ValueError:
                                    messagebox.showerror("Error", "Invalid encrypted image format!")
                                    return
                        elif message_length is not None and index < message_length + 3:
                            ascii_values.append(img[i, j, k])
                            index += 1
                        else:
                            break
                    if index >= message_length + 3:
                        break
                if index >= message_length + 3:
                    break
            
            if message_length is None:
                messagebox.showerror("Error", "Decryption failed: Message length not found.")
                return
            
            message = "".join(map(chr, ascii_values[3:]))
            
            # Create custom message box
            result_window = tk.Toplevel()
            result_window.title("Decrypted Message")
            result_label = tk.Label(result_window, text=f"Decrypted Message:\n{message}", wraplength=300)
            result_label.pack(padx=20, pady=20)
            ok_button = ModernButton(result_window, text="OK", command=result_window.destroy)
            ok_button.pack(pady=10)
        
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Main application entry point
if __name__ == "__main__":
    root = tk.Tk()
    app = SteganographyApp(root)
    root.mainloop()