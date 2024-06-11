def add(a, b):
    return a + b
import hashlib

def generate_sha256(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()
import random
import string

def generate_password(length=8):
    if not 8 <= length <= 12:
        raise ValueError("Password length must be between 8 and 12 characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
