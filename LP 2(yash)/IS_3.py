# DES using built-in only (simplified DES logic)

def pad(text):
    while len(text) % 8 != 0:
        text += ' '
    return text


def des_encrypt(text, key):
    text = pad(text)
    key_val = sum(ord(c) for c in key)

    result = ''
    for i, c in enumerate(text):
        result += chr((ord(c) + key_val + i) % 256)

    return result


def des_decrypt(cipher, key):
    key_val = sum(ord(c) for c in key)

    result = ''
    for i, c in enumerate(cipher):
        result += chr((ord(c) - key_val - i) % 256)

    return result.strip()


key = "8bytekey"
text = "HelloDES"

enc = des_encrypt(text, key)
dec = des_decrypt(enc, key)

print("Original :", text)
print("Encrypted:", enc.encode())
print("Decrypted:", dec)