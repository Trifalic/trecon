# trecon

A simple, modular, and effective Python-based reconnaissance tool designed for network and domain information gathering. Perfect for learning and expanding into real-world penetration testing workflows.

---

## 🚀 Features

* Resolve IP address of a hostname
* Retrieve Name Servers (NS records)
* Retrieve Mail Servers (MX records)
* Grab basic HTTP banner from port 80
* Perform multithreaded open port scanning
* Save the full output to a file for later analysis

---

## ⚙️ Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/trecon.git
   cd trecon
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## 📋 Usage

```bash
python recon.py <hostname> -i <initial_port> -f <final_port> -o <output_file>
```

### Example:

```bash
python recon.py example.com -i 20 -f 1024 -o result.txt
```

---

## 🎯 Arguments

* `<hostname>`: Target domain or IP to scan
* `-i`, `--initial`: Starting port for port scanning
* `-f`, `--final`: Ending port for port scanning
* `-o`, `--output`: (Optional) Save full output to a file

---

## ⚡ Next Steps (Planned)

* Add HTTPS support for Whois class
* Improve exception handling
* Add progress indicator for port scanning
* Implement IP range scanning

---

## 🚨 Disclaimer

Use this tool responsibly and only against systems you own or have explicit permission to scan. Misuse is your own problem.

---

Made with savage determination by Tanishq 💻🔥
