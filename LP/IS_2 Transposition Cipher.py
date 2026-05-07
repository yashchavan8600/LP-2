# Assignment 02 – Transposition Cipher

def encrypt(message, key):
    cipher = [''] * key

    for col in range(key):
        pointer = col

        while pointer < len(message):
            cipher[col] += message[pointer]
            pointer += key

    return ''.join(cipher)


def decrypt(cipher, key):
    num_rows = len(cipher) // key + (len(cipher) % key != 0)
    num_shaded = (key * num_rows) - len(cipher)

    plain = [''] * num_rows
    col, row = 0, 0

    for symbol in cipher:
        plain[row] += symbol
        row += 1

        if (row == num_rows) or (row == num_rows - 1 and col >= key - num_shaded):
            row = 0
            col += 1

    return ''.join(plain)


message = input("Enter message : ")
key = int(input("Enter key (cols): "))

enc = encrypt(message, key)
dec = decrypt(enc, key)

print("Encrypted:", enc)
print("Decrypted:", dec)