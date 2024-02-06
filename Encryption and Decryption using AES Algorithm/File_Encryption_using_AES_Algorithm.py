from tkinter import *
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Protocol.KDF import PBKDF2

root = Tk(className=" Text Encryptor and Decryptor")
root.geometry("400x200")

KEY_FILE = 'key.bin'  # File to store the key

def generate_key(password, salt):
    return PBKDF2(password.encode('utf-8'), salt, dkLen=32)

def save_key_to_file(key):
    with open(KEY_FILE, 'wb') as f:
        f.write(key)

def load_key_from_file():
    with open(KEY_FILE, 'rb') as f:
        return f.read()

def encrypt_file(file_type):
    file = filedialog.askopenfile(mode='rb', filetypes=[(f'text file', f'*.txt') ])
    if file:
        try:
            file_name = file.name

            password = "myPassword"  
            salt = b'YourUniqueSaltValue'
            key = generate_key(password, salt)

            with open(file_name, 'rb') as f:
                data = f.read()

            cipher = AES.new(key, AES.MODE_CBC)
            ciphered_data = cipher.encrypt(pad(data, AES.block_size))

            with open(file_name, 'wb') as f:
                f.write(cipher.iv)
                f.write(ciphered_data)

        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

def decrypt_file(file_type):
    file = filedialog.askopenfile(mode='rb', filetypes=[(f'text file', f'*.txt') ])
    if file:
        try:
            file_name = file.name

            password = "myPassword"  
            salt = b'YourUniqueSaltValue'
            key = generate_key(password, salt)

            with open(file_name, 'rb') as f:
                iv = f.read(16)
                encrypted_data = f.read()

            cipher = AES.new(key, AES.MODE_CBC, iv=iv)
            decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

            with open(file_name, 'wb') as f:
                f.write(decrypted_data)

        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

encrypt_text_button = Button(root, text="Encrypt Text File", command=lambda: encrypt_file('txt'))
encrypt_text_button.place(x=40, y=80)

decrypt_text_button = Button(root, text="Decrypt Text File", command=lambda: decrypt_file('txt'))
decrypt_text_button.place(x=200, y=80)


root.mainloop()
