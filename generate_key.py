# generate_key.py
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    print("Generated Fernet Key:", key.decode())
    return key

if __name__ == "__main__":
    generate_key()