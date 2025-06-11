from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = b"ThisIsASecretKey"  # 16 bytes
iv = b"ThisIsAnIV123456"   # 16 bytes

with open("db/init.sql", "rb") as f:
    data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
ciphertext = cipher.encrypt(pad(data, AES.block_size))

with open("db/encrypted.sql", "wb") as f:
    f.write(ciphertext)
