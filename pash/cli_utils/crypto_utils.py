from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    file_key = os.path.abspath("../secret.key")
    with open(file_key, "wb") as key_file:
        key_file.write(key)

def load_key():
    file_key = os.path.abspath("../secret.key")
    return open(file_key, "rb").read()

class Crypto:
    def encrypt_message(self,text):
        key = load_key()
        encoded_message = text.encode()
        f = Fernet(key)
        encrypted_message = f.encrypt(encoded_message)
        return encrypted_message

    def decrypt_message(self,text):
        text = text.encode("utf-8")
        key = load_key()
        f = Fernet(key)
        decrypted_message = f.decrypt(text)

        return decrypted_message.decode()