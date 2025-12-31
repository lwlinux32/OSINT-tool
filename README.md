# Modular OSINT Tool

A simple, modular Open Source Intelligence (OSINT) tool written in Python. It supports reconnaissance on Usernames, Emails, Domains, IPs, and Phone Numbers.

## Features
- **Username Recon**: Check existence of usernames across 20+ social media platforms.
- **Email Recon**: Validate syntax and check MX records.
- **Domain Recon**: Fetch DNS records and WHOIS information.
- **IP Recon**: Geolocation and reverse DNS lookups.
- **Phone Recon**: Parsing, validation, carrier, and region extraction.

## Installation

### Prerequisites
You need **Python 3.x** and **Git** installed on your system.

### 1. Install System Dependencies

Choose your operating system below:

#### Debian / Ubuntu / Kali Linux
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv git -y
```

#### Arch Linux / Manjaro
```bash
sudo pacman -S python python-pip git
```

#### Fedora
```bash
sudo dnf install python3 python3-pip git
```

#### Termux (Android)
```bash
pkg update
pkg install python git -y
```
*> Note: On Termux, you might need to install some build dependencies if packages fail to build:*
```bash
pkg install clang libxml2 libxslt -y
```

### 2. Set Up the Project

1.  **Clone or Download** this repository to your machine.
    ```bash
    # git clone https://github.com/lwlinux32/OSINT-tool.git
    # cd osint-tool
    ```


2.  **Install Python Libraries**
    ```bash
    pip install -r requirements.txt
    ```
   ## Note: "Externally managed enviroment"(PEP 6xx) or the "HINT:this package was installed by debian." errors(solved)
     pip has a LOT of errors in linux so,the solvings for the installings are followed by:  
   
   # Breaking the system packages
 by using the   ```--break-system-packages ``` and   ```--ignore-installed ``` your errors will be gone! But, breaking the system packages can make other errors so it is NOT recommended. The command will be:
    ```bash
     pip install requirements.txt -r --break-system-packages --ignore-installed
    ```
   # Create a Virtual Environment (recommended) 
      
    
    *Debian/Ubuntu/Arch/Fedora:*
    ```bash
    python3 -m venv venv
    source venv/bin/activate
     ```
    
    *Termux:*
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
    *(You will see `(venv)` appear in your terminal prompt)*
## Usage

Run the tool using `python main.py` followed by the command and target.

**Help Menu:**
```bash
python main.py --help
```

**Examples:**

*   **Username Search:**
    ```bash
    python main.py username "johndoe"
    ```

*   **Email Analysis:**
    ```bash
    python main.py email "target@example.com"
    ```

*   **Domain Information:**
    ```bash
    python main.py domain "google.com"
    ```

*   **IP Geolocation:**
    ```bash
    python main.py ip "8.8.8.8"
    ```

*   **Phone Number Info:**
    *(Use international format starting with +)*
    ```bash
    python main.py phone "+14155552671"
    ```

## Another Notes
- Some aggressive rate-limiting by websites might affect Username reconnaissance.
- WHOIS lookups utilize the system's `whois` capabilities or python library fallbacks.
