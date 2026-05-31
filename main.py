import customtkinter as ctk
from tkinter import filedialog
import encryption
import file_handler
import base64

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("AES Secure Vault")
app.geometry("900x650")

# Generate AES-256 Key
key = encryption.generate_key()

# Title
title = ctk.CTkLabel(
    app,
    text="AES Secure Vault",
    font=("Arial", 30, "bold")
)
title.pack(pady=20)

# Input Text Box
textbox = ctk.CTkTextbox(
    app,
    width=700,
    height=120
)
textbox.pack(pady=10)

# Output Text Box
resultbox = ctk.CTkTextbox(
    app,
    width=700,
    height=120
)
resultbox.pack(pady=10)

# Key Display
key_label = ctk.CTkLabel(
    app,
    text="Generated AES-256 Key"
)
key_label.pack()

key_entry = ctk.CTkEntry(
    app,
    width=700
)
key_entry.pack(pady=10)

key_entry.insert(
    0,
    base64.b64encode(key).decode()
)

# Encrypt Text
def encrypt_btn():

    text = textbox.get(
        "1.0",
        "end"
    ).strip()

    if not text:
        return

    encrypted = encryption.encrypt_text(
        text,
        key
    )

    resultbox.delete(
        "1.0",
        "end"
    )

    resultbox.insert(
        "end",
        encrypted
    )

# Decrypt Text
def decrypt_btn():

    encrypted_text = resultbox.get(
        "1.0",
        "end"
    ).strip()

    try:

        decrypted = encryption.decrypt_text(
            encrypted_text,
            key
        )

        resultbox.delete(
            "1.0",
            "end"
        )

        resultbox.insert(
            "end",
            decrypted
        )

    except Exception:

        resultbox.delete(
            "1.0",
            "end"
        )

        resultbox.insert(
            "end",
            "Invalid Cipher Text"
        )

# Encrypt File
def encrypt_file_btn():

    filepath = filedialog.askopenfilename()

    if filepath:

        output = file_handler.encrypt_file(
            filepath,
            key
        )

        resultbox.delete(
            "1.0",
            "end"
        )

        resultbox.insert(
            "end",
            f"Encrypted File Saved:\n{output}"
        )

# Decrypt File
def decrypt_file_btn():

    filepath = filedialog.askopenfilename()

    if filepath:

        output = file_handler.decrypt_file(
            filepath,
            key
        )

        resultbox.delete(
            "1.0",
            "end"
        )

        resultbox.insert(
            "end",
            f"Decrypted File Saved:\n{output}"
        )

# Buttons
encrypt_button = ctk.CTkButton(
    app,
    text="Encrypt Text",
    command=encrypt_btn
)
encrypt_button.pack(pady=5)

decrypt_button = ctk.CTkButton(
    app,
    text="Decrypt Text",
    command=decrypt_btn
)
decrypt_button.pack(pady=5)

file_encrypt_button = ctk.CTkButton(
    app,
    text="Encrypt File",
    command=encrypt_file_btn
)
file_encrypt_button.pack(pady=5)

file_decrypt_button = ctk.CTkButton(
    app,
    text="Decrypt File",
    command=decrypt_file_btn
)
file_decrypt_button.pack(pady=5)

app.mainloop()