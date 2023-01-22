import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend


def get_key(password):

    password = password.encode('utf-8')
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(password)
    return base64.urlsafe_b64encode(digest.finalize())


def encrypt(password, json):
    f = Fernet(get_key(password))
    # opening the original file to encrypt
    with open(json, 'rb') as file:
        token = file.read()
    en = f.encrypt(bytes(token))

    with open('.//src//cryptography_sandbox//encrypted_json.json', 'wb') as encrypted_file:
        encrypted_file.write(en)


def decrypt(password, json):
    f = Fernet(get_key(password))

    # opening the original file to deencrypt
    with open(json, 'rb') as encrypted_file:
        token = encrypted_file.read()
    dec = f.decrypt(bytes(token))
    with open('.//src//cryptography_sandbox//decrypted_json.json', 'wb') as file:
        file.write(dec)

 
if __name__ == '__main__':
    encrypt('abc','.//src//cryptography_sandbox//og.json')
    decrypt('abc','.//src//cryptography_sandbox//encrypted_json.json')