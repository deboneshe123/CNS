from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def encrypt_file(filepath, key):

    with open(filepath, "rb") as file:
        data = file.read()

    cipher = AES.new(key, AES.MODE_CBC)

    encrypted_data = cipher.iv + cipher.encrypt(
        pad(data, AES.block_size)
    )

    filename = os.path.basename(filepath)

    output_path = (
        "encrypted_files/"
        + filename
        + ".enc"
    )

    with open(output_path, "wb") as file:
        file.write(encrypted_data)

    return output_path

def decrypt_file(filepath, key):

    with open(filepath, "rb") as file:
        data = file.read()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = AES.new(
        key,
        AES.MODE_CBC,
        iv=iv
    )

    decrypted_data = unpad(
        cipher.decrypt(ciphertext),
        AES.block_size
    )

    filename = os.path.basename(filepath)

    output_path = (
        "decrypted_files/decrypted_"
        + filename.replace(".enc", "")
    )

    with open(output_path, "wb") as file:
        file.write(decrypted_data)

    return output_path