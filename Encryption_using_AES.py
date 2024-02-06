# from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2        # makes brute-force attacks more difficult
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad    # adding extra bits to match the block size

salt = b'J\x98\xd2\x83\xe4\x8az\xb8\xe0\x18\xac\x96`\x0b\tr\x9e\x02\x06\xd4\xa9]\xf8"0\x1d\x15\x00>\xd1\x9c\xbf'
password = "mypassword"

key = PBKDF2(password, salt, dkLen=32)

message = b"Text you want to encrypt"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

with open('encrypted.bin', 'wb') as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
    print('The encrypted form of the text: ', ciphered_data)

with open('encrypted.bin', 'rb') as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)
print('The original text: ', original)

with open('key.bin', 'wb') as f:
    f.write(key)
