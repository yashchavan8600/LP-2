# first install crypto lib if it's not there
# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# --- User Input ---
key = input("Enter 16-byte key: ").encode()
text = input("Enter text: ").encode()

cipher = AES.new(key, AES.MODE_ECB)

encrypted = cipher.encrypt(pad(text, 16))
decrypted = unpad(cipher.decrypt(encrypted), 16)

print(encrypted)
print(decrypted)