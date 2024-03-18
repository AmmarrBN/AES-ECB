# Ngapain bang? Minimal Credit cuihh
# Copyright 2024 ©AmmarBN
# https://github.com/AmmarrBN/AES-ECB

import os,sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import random

def encrypt_code(code, key):
    watermark = "Made By AmmarBN"
    # Add watermark to the code before encryption
    code_with_watermark = f"{code}\n# Watermark: {watermark}"
    cipher = AES.new(key, AES.MODE_ECB)
    padded_code = pad(code_with_watermark.encode(), AES.block_size)
    encrypted_code = cipher.encrypt(padded_code)
    return base64.b64encode(encrypted_code).decode('utf-8')

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_message = cipher.decrypt(encrypted_message)
    return unpad(decrypted_message, AES.block_size).decode('utf-8')

def banner():
    print ("""

  __   ____  ____        ____  ___  ____
 / _\ (  __)/ ___)  ___ (  __)/ __)(  _ )
/    \ ) _) \___ \ (___) ) _)( (__  ) _ (
\_/\_/(____)(____/      (____)\___)(____/

 • Creator: AmmarBN
 • Github : github.com/AmmarrBN
 • Info   : AES-ECB Python3 Encryption
""")

def main():
    os.system("clear")
    banner()
    input_file = input(" • Enter File Name (exam:main.py): ")

    try:
        with open(input_file, 'r') as file:
            code = file.read()
    except FileNotFoundError:
        print("File not found.")
        return

    # Generate random 16-byte key
    key = bytes([random.randint(0, 255) for _ in range(16)])
    
    # Encrypt source code
    encrypted_code = encrypt_code(code, key)
    
    # Encrypt access denied message
    access_denied_message = "Cannot run: Credit has been removed, access denied"
    encrypted_message = encrypt_message(access_denied_message, key)

    # Define variable c
    c = base64.b64encode('Made By AmmarBN'.encode()).decode('utf-8')
    
    output_file = input_file.split('.')[0] + "_encrypted.py"

    with open(output_file, 'w') as file:
        file.write(f"import base64\n")
        file.write(f"from Crypto.Cipher import AES\n")
        file.write(f"from Crypto.Util.Padding import unpad\n")
        file.write(f"import sys\n")
        file.write(f"key = {key}\n")
        file.write(f"cipher = AES.new(key, AES.MODE_ECB)\n")
        file.write(f"encrypted_code = base64.b64decode('{encrypted_code}')\n")
        file.write(f"decrypted_code = unpad(cipher.decrypt(encrypted_code), AES.block_size).decode('utf-8')\n")
        file.write(f"run_code = lambda c: exec(decrypted_code, globals()) if base64.b64decode('{c}').decode('utf-8') == 'Made By AmmarBN' else sys.exit(decrypt_message(base64.b64decode('{base64.b64encode(encrypted_message).decode()}'), key))\n")
        file.write(f"try:\n")
        file.write(f"    run_code('{c}')\n")
        file.write(f"except Exception as e:\n")
        file.write(f"    print('Error during execution:', e)\n")
        file.write(f"    sys.exit(1)\n")

    print("File has been successfully encrypted. Encrypted file is saved as:", output_file)

if __name__ == "__main__":
    main()
