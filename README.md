# mcafee-xpass
`mcafee-xpass` is a lightweight Python tool for extracting and decrypting administrator passwords from McAfee's `Sitelist.xml` configuration files. It decodes base64-encoded, XOR-obfuscated, and 3DES-encrypted password fields using a known static key and decryption scheme.

### ⚙️ Features

- Supports direct base64 decryption input
- Cleans non-printable padding artifacts
- Designed for terminal or automation use
- Compatible with Python 3.x

### 📦 Installation
```
git clone https://github.com/<your-username>/mcafee-xpass.git
```

```
cd mcafee-xpass
```
```
pip install -r requirements.txt
```

### 🧰 Requirements
* Python 3.6+
* pycryptodome library

### 🧪 Example
```bash
python3 mcafee_xpass.py 'jWbTyS7BL1Hj7PkO5Di/QhhYmcGj5cOoZ2OkDTrFXsR/abAFPM9B3Q=='
[+] Encrypted Password : jWbTyS7BL1Hj7PkO5Di/
QhhYmcGj5cOoZ2OkDTrFXsR/abAFPM9B3Q==
[+] Decrypted Password : MyStrongPassword!
```

### 📄 License
MIT License. See LICENSE file for details.

### 👨‍💻 Author
Originally by @funoverip.
Improved and maintained by Sujal Meghwal.

### 🔐 Disclaimer
> This tool is provided for educational, forensic, and authorized security testing use only.Do not use against systems you do not own or have explicit permission to test.
