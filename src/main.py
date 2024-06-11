import random
import string
import hashlib

def add(a, b):
    return a + b

def generate_password(length=8):
    if not 8 <= length <= 12:
        raise ValueError("Password length must be between 8 and 12 characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def generate_sha256(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
