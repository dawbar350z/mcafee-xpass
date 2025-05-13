#!/usr/bin/env python3
"""
McAfee Sitelist.xml Password Decryption Tool

Author   : Sujal Meghwal
Updated  : May 2025 by Sujal Meghwal
Original : https://github.com/funoverip/mcafee-sitelist-pwd-decryption

Usage:
    python3 mcafee-xpass.py <base64_encrypted_password>

Example:
    python3 mcafee-xpass.py 'jWbTyS7BL1Hj7PkO5Di/QhhYmcGj5cOoZ2OkDTrFXsR/abAFPM9B3Q=='
"""

import sys
import base64
from Cryptodome.Cipher import DES3
from Cryptodome.Hash import SHA1

# Hardcoded XOR key used in McAfee Sitelist obfuscation
XOR_KEY = bytearray.fromhex("12150F10111C1A060A1F1B1817160519").decode("utf-8")

def sitelist_xor(data: bytes) -> bytes:
    """Applies McAfee XOR transformation using the known static key."""
    return bytes([b ^ ord(XOR_KEY[i % len(XOR_KEY)]) for i, b in enumerate(data)])

def des3_ecb_decrypt(data: bytes) -> bytes:
    """
    Decrypts the XOR'd data using 3DES-ECB with a static key derived from SHA1 hash of '<!@#$%^>'.
    """
    key_material = SHA1.new(b'<!@#$%^>').digest() + bytes(4)  # Total 24 bytes
    cipher = DES3.new(key_material, DES3.MODE_ECB)

    # McAfee may not pad to 8 bytes correctly; pad manually if needed
    padded_data = data + b'\x00' * ((8 - len(data) % 8) % 8)

    decrypted = cipher.decrypt(padded_data)
    # Strip possible null bytes from the end
    return decrypted.rstrip(b'\x00')

def main():
    if len(sys.argv) != 2:
        print("Usage   : %s <base64_encrypted_password>" % sys.argv[0])
        print("Example : %s 'base64string=='" % sys.argv[0])
        sys.exit(1)

    try:
        encrypted_b64 = sys.argv[1]
        encrypted_bytes = base64.b64decode(encrypted_b64)
    except Exception as e:
        print(f"[!] Error decoding base64 input: {e}")
        sys.exit(1)

    xor_decrypted = sitelist_xor(encrypted_bytes)
    final_plaintext = des3_ecb_decrypt(xor_decrypted)

    try:
        decoded_password = final_plaintext.decode("utf-8")
    except UnicodeDecodeError:
        decoded_password = final_plaintext.decode("latin-1")  # Fallback for weird encodings

    print("[+] Encrypted Password : %s" % encrypted_b64)
    print("[+] Decrypted Password : %s" % decoded_password if decoded_password else "<empty>")

if __name__ == "__main__":
    main()
