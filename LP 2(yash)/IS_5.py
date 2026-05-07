# RSA using built-in only (math module)

import math


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d
    return None


# Key generation
p, q = 61, 53
n = p * q
phi = (p - 1) * (q - 1)
e = 17  # public exponent
d = mod_inverse(e, phi)

print(f"Public Key : (e={e}, n={n})")
print(f"Private Key : (d={d}, n={n})")


# Encrypt
message = 65  # ASCII 'A'
encrypted = pow(message, e, n)

# Decrypt
decrypted = pow(encrypted, d, n)

print(f"Original : {message} -> '{chr(message)}'")
print(f"Encrypted : {encrypted}")
print(f"Decrypted : {decrypted} -> '{chr(decrypted)}'")