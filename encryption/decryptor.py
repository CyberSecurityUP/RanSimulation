import os
from cryptography.fernet import Fernet

def decrypt_files(path, key, encrypted_extension=".locked"):
    fernet = Fernet(key)
    for root, _, files in os.walk(path):
        for file in files:
            filepath = os.path.join(root, file)
            if not filepath.endswith(encrypted_extension):
                continue
            with open(filepath, 'rb') as f:
                encrypted_data = f.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            original_filepath = filepath.replace(encrypted_extension, "")
            with open(original_filepath, 'wb') as f:
                f.write(decrypted_data)
            os.remove(filepath)
