from tkinter import *
from tkinter import filedialog

root = Tk(className=" Image Encryptor and Decryptor")
root.geometry("300x180")


def encrypt_image():
    file = filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg'), ('png file', '*.png')])
    if file is not None:
        file_name = file.name
        key = text_box.get(1.0, END)
        print(file_name, key)
        f = open(file_name, 'rb')
        image = f.read()
        f.close()
        image = bytearray(image)
        for index, values in enumerate(image):    # used enumerate to use the same definition for encryption and decryption
            image[index] = values ^ int(key)
        fil = open(file_name, 'wb')
        fil.write(image)
        fil.close()


button = Button(root, text=" Click to encrpyt/decrypt", command=encrypt_image)
button.place(x=40, y=80)

label = Label(root, text="Enter a key to encrypt/decrypt")
label.place(x=40, y=20)
text_box = Text(root, height=1, width=14)
text_box.place(x=80, y=50)

root.mainloop()
