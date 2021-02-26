from cryptography.fernet import Fernet
import os
import colorama
import click

colorama.init()

def generate_key():
    key = Fernet.generate_key()
    file_key = os.path.abspath("pash/secret.key")
    with open(file_key, "wb") as key_file:
        key_file.write(key)

def load_key():
    try:
        file_key = os.path.abspath("pash/secret.key")
        return open(file_key, "rb").read()
    except:
        click.secho("An error with your crypto key", fg = "red")
        return False

class Crypto:
    def encrypt_message(self,text):
        key = load_key()
        if key:
            encoded_message = text.encode()
            f = Fernet(key)
            encrypted_message = f.encrypt(encoded_message)
            return encrypted_message

    def decrypt_message(self,text):
        key = load_key()
        if key:
            f = Fernet(key)
            decrypted_message = f.decrypt(text)
            return decrypted_message.decode()