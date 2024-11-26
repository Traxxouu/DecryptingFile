import os
from tkinter import Tk, Label, Button, Frame, filedialog, messagebox
from cryptography.fernet import Fernet

class EncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encryption/Decryption Tool")

        title_label = Label(root, text="""
 ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░  ░▒▓█▓▒░     
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░     
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░     
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░   ░▒▓█▓▒░        ░▒▓█▓▒░     
                                                                  
                                                                  
""", font=("Helvetica", 12))
        title_label.pack(pady=10)

        # Frame - Buttons
        button_frame = Frame(root)
        button_frame.pack(pady=10)

        # Buttons
        Button(button_frame, text="Generate Key", command=self.generate_key,
               font=("Helvetica", 14), width=20, height=2).pack(pady=10)
        Button(button_frame, text="Encrypt File", command=self.encrypt_file,
               font=("Helvetica", 14), width=20, height=2).pack(pady=10)
        Button(button_frame, text="Decrypt File", command=self.decrypt_file,
               font=("Helvetica", 14), width=20, height=2).pack(pady=10)

        # Status
        self.status_label = Label(root, text="", fg="green", font=("Helvetica", 12))
        self.status_label.pack(pady=10)

    def generate_key(self):
        key = Fernet.generate_key()
        with open("encryption_key.key", "wb") as key_file:
            key_file.write(key)
        messagebox.showinfo("Key Generated", "Key saved as 'encryption_key.key'")

    def encrypt_file(self):
        key_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
        if not key_path:
            return
        file_to_encrypt = filedialog.askopenfilename(title="Select File to Encrypt")
        if not file_to_encrypt:
            return
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        with open(file_to_encrypt, "rb") as file:
            data = file.read()
        encrypted_data = cipher.encrypt(data)
        encrypted_file = file_to_encrypt + ".encrypted"
        with open(encrypted_file, "wb") as file:
            file.write(encrypted_data)
        messagebox.showinfo("Encryption Successful", f"Encrypted file saved as '{encrypted_file}'")

    def decrypt_file(self):
        key_path = filedialog.askopenfilename(title="Select Key File", filetypes=[("Key Files", "*.key")])
        if not key_path:
            return
        file_to_decrypt = filedialog.askopenfilename(title="Select File to Decrypt")
        if not file_to_decrypt:
            return
        with open(key_path, "rb") as key_file:
            key = key_file.read()
        cipher = Fernet(key)
        with open(file_to_decrypt, "rb") as file:
            encrypted_data = file.read()
        try:
            decrypted_data = cipher.decrypt(encrypted_data)
            decrypted_file = os.path.splitext(file_to_decrypt)[0] + "_decrypted.txt"
            with open(decrypted_file, "wb") as file:
                file.write(decrypted_data)
            messagebox.showinfo("Decryption Successful", f"Decrypted file saved as '{decrypted_file}'")
        except Exception as e:
            messagebox.showerror("Decryption Failed", "Invalid key or corrupted file")

# Run
if __name__ == "__main__":
    root = Tk()
    app = EncryptionApp(root)
    root.geometry("1000x600")
    root.mainloop()
