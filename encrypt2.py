# encrypt_sql.py
from cryptography.fernet import Fernet
import os
import sys

# Use the key you generated (replace with your actual key)
KEY = b'dnmZ-hdSUsO3pZLLaXJkUdJ-mbW6KwFpPMKxIteNRCs='  # Example key - use your generated one

def encrypt_file(input_file, output_file):
    try:
        fernet = Fernet(KEY)
        
        # Read SQL file
        with open(input_file, 'rb') as f:
            original = f.read()
        
        # Encrypt and write
        encrypted = fernet.encrypt(original)
        with open(output_file, 'wb') as f:
            f.write(encrypted)
        
        print(f"Successfully encrypted {input_file} to {output_file}")
        return True
    except Exception as e:
        print(f"Encryption failed: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypt_sql.py <input_file> <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found")
        sys.exit(1)
    
    encrypt_file(input_file, output_file)