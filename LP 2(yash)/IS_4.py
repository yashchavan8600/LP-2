# AES using built-in only (simplified AES logic)

def pad(text, block=16):
    while len(text) % block != 0:
        text += ' '
    return text


def aes_encrypt(text, key):
    text = pad(text)
    key_vals = [ord(c) for c in key]

    result = ''
    for i, c in enumerate(text):
        shift = key_vals[i % len(key_vals)]
        result += chr((ord(c) ^ shift + i) % 256)

    return result


def aes_decrypt(cipher, key):
    key_vals = [ord(c) for c in key]

    result = ''
    for i, c in enumerate(cipher):
        shift = key_vals[i % len(key_vals)]
        result += chr((ord(c) ^ shift + i) % 256)

    return result.strip()


key = "0123456789abcdef"
text = "HelloAESWorld!!"

enc = aes_encrypt(text, key)
dec = aes_decrypt(enc, key)

print("Original :", text)
print("Encrypted:", enc.encode())
print("Decrypted:", dec)