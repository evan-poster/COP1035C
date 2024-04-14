#!/usr/bin/env python3
# Week2/Ch4 Exercises/program2.py

"""
Inputs:
  encrypted: A string of encrypted text
  distance: The number of characters to shift the text
Outputs:
  Plaintext
"""

def caesar_cipher(line, distance):
    """Decrypt a line of plaintext using a Caesar Cipher"""
    decrypted = ""
    for char in line:
        # Convert char to ASCII
        ascii_char = ord(char)
        # Shift ASCII
        if 32 <= ascii_char <= 126:  # All printable ASCII characters
            ascii_char = (ascii_char - 32 - distance) % 95 + 32
        # Convert back to char
        decrypted += chr(ascii_char)
    return decrypted


if __name__ == "__main__":
    encrypted = input("Enter a line of encrypted text: ")
    distance = int(input("Enter the distance: "))
    print("Decrypted:", caesar_cipher(encrypted, distance))
