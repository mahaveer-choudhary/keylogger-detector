<div align="center">
  <h1>🛡️ Keylogger Detector</h1>
  <p><i>A powerful Python utility to scan, detect, and terminate keyloggers on your system.</i></p>

  [![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
  [![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey)](#)
  [![License](https://img.shields.io/badge/License-MIT-green)](#)
</div>

---

## 📖 Description 

This **Keylogger Detector** is an advanced Python script designed to actively identify and locate potential keyloggers running on a system. It provides an extra layer of security by scanning directories for keylogger patterns and dynamically monitoring active network processes. It intercepts malicious programs attempting to send logged keystrokes from your device and provides you with the tools to take immediate action.

### ✨ Key Features
- **Static File Scanning**: Scan specific directories or drives for Python scripts exhibiting common keylogger behavior patterns.
- **Dynamic Connection Monitoring**: Track active processes attempting to communicate over targeted SMTP ports.
- **Actionable Defense**: Terminate malicious processes, delete host files, or investigate their exact system locations.
- **Whitelist/Blacklist Manager**: Safely mark trusted processes to avoid false positives in future scans.
- **Modern CLI Interface**: A beautifully formatted, interactive dashboard utilizing `rich` and `colorama`.

---

## 📡 Email / SMTP Monitoring 

Keyloggers typically log keystrokes locally for a fixed period before attempting to send the log file to an attacker via email. Operating dynamically, Keylogger Detector monitors the most frequently abused SMTP ports to catch these connections in the act.

#### Popular SMTP servers monitored to detect exfiltration:
| Mail Provider | Security Type | Port |
| :--- | :--- | :--- |
| **Gmail** (`smtp.gmail.com`) | SSL | 465 |
| **Gmail** (`smtp.gmail.com`) | StartTLS | 587 |
| **Outlook / Live** (`smtp.live.com`) | StartTLS | 587 |
| **Office 365** (`smtp.office365.com`) | StartTLS | 587 |
| **Yahoo Mail** (`smtp.mail.yahoo.com`) | StartTLS | 587 |
*(Also actively monitors port `2525`)*

---

## ⚙️ Installation 

To use the Keylogger detector, follow these steps: 

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/mahaveer-choudhary/keylogger-detector
   cd keylogger-detector
   ```

2. **Install Required Dependencies**:
   The tool utilizes libraries like `psutil`, `rich`, and `colorama`. Ensure you have Python installed and run:
   ```bash
   pip install psutil rich colorama
   ```

3. **Run the script**:
   ```bash
   # On Linux (sudo is recommended for full port tracking)
   sudo python3 keylogger-detector.py

   # On Windows (Run Command Prompt/Powershell as Administrator)
   python keylogger-detector.py
   ```

---

## 🚀 Usage 

Launch the interactive dashboard to interact with the protection tools. 

1. **Main Menu**:
    Upon launching, you will be presented with a modern CLI interface:
    - `[ 1 ] Scan for a particular location`
    - `[ 2 ] Detect keylogger automatically`
    - `[ 3 ] Exit`

2. **Taking Action**:
    - If a threat is detected during the active network monitor (`Option 2`), the console will alert you immediately.
    - You will be given sub-options to **Find Location**, **Terminate Process**, **Remove File**, or manage your **Whitelists** to refine scanning over time.

---

### 📸 Screenshots

<details>
<summary>Click to view interface screenshots</summary>
<br>

![Interface 1](https://drive.google.com/uc?export=view&id=1gz11l-cM2_yQqo9hI1ZtIFadRA_KLUDH)

![Interface 2](https://drive.google.com/uc?export=view&id=1tYl4sIZIH2Kfm8UbI1wZPpaQTLBAWk8G)

![Interface 3](https://drive.google.com/uc?export=view&id=1F2QmNXrDn2qm-DEq5pjABszVzwZdR0Th)

</details>
