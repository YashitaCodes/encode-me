import tkinter as tk
from tkinter import messagebox, simpledialog
from encoders import encode_base64, hash_md5, hash_sha256, encrypt_aes
import pyperclip

class EncodingApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Text Encoder")

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.window, text="Enter Text:").grid(row=0, column=0)

        self.input_text = tk.Entry(self.window, width=50)
        self.input_text.grid(row=0, column=1)

        self.algorithm = tk.StringVar(self.window)
        self.algorithm.set("Base64")  # Default selection

        tk.Label(self.window, text="Select Algorithm:").grid(row=1, column=0)
        tk.OptionMenu(self.window, self.algorithm, "Base64", "MD5", "SHA-256", "AES").grid(row=1, column=1)

        tk.Button(self.window, text="Encode", command=self.encode_text).grid(row=2, column=0, columnspan=2)

        self.result_text = tk.Text(self.window, height=5, width=50)
        self.result_text.grid(row=3, column=0, columnspan=2)

        tk.Button(self.window, text="Copy to Clipboard", command=self.copy_to_clipboard).grid(row=4, column=0, columnspan=2)
    
    def encode_text(self):
        text = self.input_text.get()
        if not text:
            messagebox.showerror("Error", "Please enter some text.")
            return

        algorithm = self.algorithm.get()

        if algorithm == "Base64":
            result = encode_base64(text)
        elif algorithm == "MD5":
            result = hash_md5(text)
        elif algorithm == "SHA-256":
            result = hash_sha256(text)
        elif algorithm == "AES":
            key = simpledialog.askstring("Input", "Enter AES Key (16, 24, or 32 bytes long):")
            result = encrypt_aes(text, key)
        else:
            result = "Unsupported Algorithm"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def copy_to_clipboard(self):
        result = self.result_text.get(1.0, tk.END).strip()
        if result:
            pyperclip.copy(result)
            messagebox.showinfo("Copied", "Result copied to clipboard!")
        else:
            messagebox.showerror("Error", "No result to copy.")

    def run(self):
        self.window.mainloop()
