# Assignment 01 – Bitwise AND and XOR on String 

s = input("Enter string: ")
print("Original String :", s)

# AND operation
and_result = ''.join(chr(ord(c) & 127) for c in s)
print("After AND with 127:", and_result)

# XOR operation
xor_result = ''.join(chr(ord(c) ^ 127) for c in s)
print("After XOR with 127 (raw):", repr(xor_result))  # safer display

# Verify reversibility of XOR
restored = ''.join(chr(ord(c) ^ 127) for c in xor_result)
print("XOR Restored   :", restored)