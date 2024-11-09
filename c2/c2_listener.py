import socket

def start_listener(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen(1)
        print(f"[*] Listening on {ip}:{port}...")
        conn, addr = s.accept()
        print(f"[+] Connection from {addr}")
        key = conn.recv(1024)
        print(f"[+] Received key: {key.decode()}")
        conn.close()
        s.close()
    except Exception as e:
        print(f"[-] Error: {e}")
