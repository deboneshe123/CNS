from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64

def generate_key():
    """
    Generate a 256-bit AES key (32 bytes)
    """
    return get_random_bytes(32)

def encrypt_text(text, key):
    """
    Encrypt text using AES-CBC
    """

    cipher = AES.new(key, AES.MODE_CBC)

    ciphertext = cipher.encrypt(
        pad(text.encode(), AES.block_size)
    )

    encrypted_data = cipher.iv + ciphertext

    return base64.b64encode(
        encrypted_data
    ).decode()

def decrypt_text(encrypted_text, key):
    """
    Decrypt AES-CBC encrypted text
    """

    encrypted_data = base64.b64decode(
        encrypted_text
    )

    iv = encrypted_data[:16]

    ciphertext = encrypted_data[16:]

    cipher = AES.new(
        key,
        AES.MODE_CBC,
        iv=iv
    )

    plaintext = unpad(
        cipher.decrypt(ciphertext),
        AES.block_size
    )

    return plaintext.decode()