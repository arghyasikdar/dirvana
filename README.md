# Dirvana

Dirvana is a lightweight Python-based directory traversal and hidden-path discovery tool.

Developed by Arghya Sikdar.

---

# Requirements

- Python 3.8 or higher
- pip3
- requests Python module

---

# Download

Download or clone the project files:

```bash
git clone https://github.com/arghyasikdar/dirvana.git
cd dirvana
```

Or manually download:

- dirvana.py
- install_dirvana.sh

Place them inside the same folder.

---

# Linux Installation

Tested on:
- Kali Linux
- Ubuntu
- Debian
- Arch Linux
- Fedora

## Step 1 — Open Terminal

Navigate to the project folder:

```bash
cd dirvana
```

---

## Step 2 — Make files executable

```bash
chmod +x dirvana.py
chmod +x install_dirvana.sh
```

---

## Step 3 — Install dependencies

```bash
pip3 install requests
```

---

## Step 4 — Install globally

```bash
sudo ./install_dirvana.sh
```

After installation, run from anywhere using:

```bash
dirvana
```

---

# macOS Installation

## Step 1 — Open Terminal

Press:

```text
CMD + SPACE
```

Search for:

```text
Terminal
```

---

## Step 2 — Navigate to the folder

```bash
cd ~/Desktop/dirvana
```

---

## Step 3 — Make files executable

```bash
chmod +x dirvana.py
chmod +x install_dirvana.sh
```

---

## Step 4 — Install dependency

```bash
pip3 install requests
```

If pip3 is missing:

Install Homebrew:

https://brew.sh

Then install Python:

```bash
brew install python
```

---

## Step 5 — Run the installer

```bash
sudo ./install_dirvana.sh
```

---

## Step 6 — Run Dirvana

```bash
dirvana
```

Or run directly:

```bash
python3 dirvana.py
```

---

# Windows Installation

## Step 1 — Install Python

Download Python:

https://www.python.org/downloads/windows/

During installation, enable:

```text
Add Python to PATH
```

---

## Step 2 — Download the project files

Place the following files inside the same folder:

```text
dirvana.py
```

---

## Step 3 — Install dependency

Open CMD or PowerShell:

```powershell
pip install requests
```

---

## Step 4 — Run Dirvana

```powershell
python dirvana.py
```

---

# Usage

Basic syntax:

```bash
python3 dirvana.py -u <target-url> -w <wordlist>
```

Example:

```bash
python3 dirvana.py -u http://testphp.vulnweb.com -w wordlist.txt
```

---

# Options

| Option | Description |
|---|---|
| -u | Target URL |
| -w | Wordlist file |
| -v | Show version |

---

# Creating a Wordlist

Create a file named:

```text
wordlist.txt
```

Example contents:

```text
admin/
backup/
uploads/
config/
logs/
../../../../etc/passwd
```

---

# Example Commands

Run a scan:

```bash
python3 dirvana.py -u http://example.com -w wordlist.txt
```

Show version:

```bash
python3 dirvana.py -v
```

---

# Example Output

```text
[200] http://target.com/admin - Page Found
[403] http://target.com/backup - Forbidden
[404] http://target.com/logs - Not Found
```

---

# Recommended Test Labs

Use only on systems you own or are authorized to test.

Safe practice environments:

- OWASP Juice Shop
- DVWA
- WebGoat
- Metasploitable

---

# Troubleshooting

## Permission denied

Run:

```bash
chmod +x dirvana.py
```

---

## pip3 command not found

Linux:

```bash
sudo apt install python3-pip
```

macOS:

```bash
brew install python
```

Windows:

Reinstall Python and enable:

```text
Add Python to PATH
```

---

# Disclaimer

This tool is intended only for:

- Educational purposes
- Ethical hacking
- Security research
- Authorized penetration testing
- CTF environments

Unauthorized use against systems without permission may be illegal.

The developer is not responsible for misuse.

---

# Author

Arghya Sikdar
Assistant Professor of Cyber Security
