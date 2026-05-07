# first install crypto lib if it's not there
# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# --- User Input ---
key = input("Enter 8-byte key: ").encode()
text = input("Enter text: ").encode()

cipher = DES.new(key, DES.MODE_ECB)

encrypted = cipher.encrypt(pad(text, 8))
decrypted = unpad(cipher.decrypt(encrypted), 8)

print(encrypted)
print(decrypted)