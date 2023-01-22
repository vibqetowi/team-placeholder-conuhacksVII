import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def get_key(password):

    password = password.encode('utf-8')
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())


def encrypt(password):
    f = Fernet(get_key(password))
    # opening the original file to encrypt
    with open('vault.json', 'rb') as file:
        token = file.read()
    en = f.encrypt(bytes(token))

    with open('.//src//server//encrypted_vault.txt', 'wb') as encrypted_file:
        encrypted_file.write(en)


def decrypt(password):
    f = Fernet(get_key(password))

    # opening the original file to deencrypt
    with open('.//src//server//encrypted_vault.txt', 'rb') as encrypted_file:
        token = encrypted_file.read()
    dec = f.decrypt(bytes(token))
    with open('.//src//server//decrypted_vault.json', 'wb') as file:
        file.write(dec)

 
if __name__ == '__main__':
    encrypt('abc')
    decrypt('abc')