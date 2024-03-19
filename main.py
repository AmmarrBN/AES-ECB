# Ngapain bang? Minimal Credit cuihh
# Copyright 2024 ©AmmarBN
# https://github.com/AmmarrBN/AES-ECB
# Recode? Credit pls

import os,sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64
import random
import marshal

def encrypt_code(code, key):
    watermark = "AmmarBN"
    # Add watermark to the code before encryption
    code_with_watermark = f"{code}\n# Watermark: {watermark}"
    # Compile the code into a code object
    compiled_code = compile(code_with_watermark, '<string>', 'exec')
    # Convert the compiled code into bytecode
    bytecode = marshal.dumps(compiled_code)
    cipher = AES.new(key, AES.MODE_ECB)
    padded_bytecode = pad(bytecode, AES.block_size)
    encrypted_bytecode = cipher.encrypt(padded_bytecode)
    return base64.b64encode(encrypted_bytecode).decode('utf-8')

def encrypt_message(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_message = pad(message.encode(), AES.block_size)
    encrypted_message = cipher.encrypt(padded_message)
    return base64.b64encode(encrypted_message).decode('utf-8')

def obfuscate_code(code):
    # Example obfuscation technique: replace all occurrences of 'exec' with 'x_x_e_c'
    obfuscated_code = code.replace('exec', 'x_x_e_c')
    return obfuscated_code

def clear_terminal():
    # Untuk Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Untuk MacOS dan Linux
    else:
        _ = os.system('clear')

# Panggil fungsi clear_terminal() untuk membersihkan terminal
# clear_terminal()

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
    clear_terminal()
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
    
    # Obfuscate source code
    obfuscated_code = obfuscate_code(code)
    
    # Encrypt source code
    encrypted_code = encrypt_code(obfuscated_code, key)
    
    # Encrypt access denied message
    access_denied_message = "Cannot run: Credit has been removed, access denied"
    encrypted_message = encrypt_message(access_denied_message, key)

    # Define variable c
    c = base64.b64encode('AmmarBN'.encode()).decode('utf-8')
    
    output_file = input_file.split('.')[0] + "_encrypted.py"

    with open(output_file, 'w') as file:
        file.write(f"import base64\n")
        file.write(f"aes_ebc=(")
        for _ in range(3000):
           file.write('"😁","💀","🥶","😆","🤣","😘","😜","😁","💀","🥶","😆","🤣","😘","😜","😁","💀","🥶","😆","🤣","😘","😜",\n')
        file.write(")\n")
        file.write(f"from Crypto.Cipher import AES\n")
        file.write(f"from Crypto.Util.Padding import unpad\n")
        file.write(f"import sys\n")
        file.write(f"import marshal\n")
        file.write(f"key = {key}\n")
        file.write(f"aes_ebc2=(")
        for _ in range(3000):
           file.write('"Your Wellcome","Your Wellcome","Your Wellcome","Your Wellcome","Your Wellcome",\n')
        file.write(")\n")
        file.write(f"cipher = AES.new(key, AES.MODE_ECB)\n")
        file.write(f"encrypted_code = base64.b64decode('{encrypted_code}')\n")
        file.write(f"decrypted_bytecode = unpad(cipher.decrypt(encrypted_code), AES.block_size)\n")
        file.write(f"compiled_code = marshal.loads(decrypted_bytecode)\n")
        file.write(f"x_x_e_c = exec\n")  # Define 'exec' with obfuscated name
        file.write(f"x_x_e_v = '{c}'\n")  # Define 'c' with obfuscated name
        file.write(f"run_code = lambda: x_x_e_c(compiled_code, globals())\n")  # Define lambda function
        file.write(f"try:\n")
        file.write(f"    if base64.b64decode(x_x_e_v.encode()).decode('utf-8') != 'AmmarBN':\n")
        file.write(f"        raise Exception('Cannot run: Credit has been removed, access denied')\n")
        file.write(f"    run_code()\n")  # Execute lambda function
        file.write(f"except Exception as e:\n")
        file.write(f"    print('Error during execution:', e)\n")
        file.write(f"    sys.exit(1)\n")

    print("File has been successfully encrypted. Encrypted file is saved as:", output_file)

if __name__ == "__main__":
    main()
