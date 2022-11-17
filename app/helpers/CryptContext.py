import os
import json
from passlib.context import CryptContext

with open(os.path.join(os.path.dirname(__file__), '../core/config.json'), "r") as file:
    config = json.load(file)

hash_schemes = config["hash_schemes"]

crypt_context = CryptContext(schemes=hash_schemes)

def hash_data(plainText: str):
    return crypt_context.hash(plainText)

def verify_data(plainText, encryptText):
    return crypt_context.verify(plainText, encryptText)