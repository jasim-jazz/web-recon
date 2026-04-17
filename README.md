# Advanced Web Reconnaissance Tool

This project is a Python-based web reconnaissance tool designed to automate the initial information gathering phase of security testing and bug bounty hunting.

The tool performs multiple reconnaissance tasks including domain resolution, port scanning, subdomain enumeration, directory brute-forcing, and HTTP header analysis.

---

## Features

* Multi-threaded port scanning
* Subdomain enumeration using wordlists
* Directory brute forcing
* HTTP header analysis
* Basic technology detection
* Command-line interface using argparse
* Optional output saving to file

---

## Requirements

* Python 3.x
* requests library

Install dependencies:

```bash
pip install requests
```

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/web-recon-tool.git
cd web-recon-tool
```

---

## Usage

```bash
python3 recon.py <target> [options]
```

---

## Arguments

| Argument      | Description                           |
| ------------- | ------------------------------------- |
| target        | Target URL (e.g., http://example.com) |
| -t, --threads | Number of threads (default: 50)       |
| -o, --output  | Save results to a file                |

---

## Examples

Basic scan:

```bash
python3 recon.py http://example.com
```

Custom thread count:

```bash
python3 recon.py http://example.com -t 100
```

Save output:

```bash
python3 recon.py http://example.com -o results.txt
```

---

## How It Works

1. Resolves the domain to an IP address
2. Scans common ports using multi-threading
3. Retrieves HTTP headers and identifies technologies
4. Enumerates common subdomains
5. Performs directory brute-forcing on common paths
6. Displays and optionally saves the results

---

## Example Output

```
[+] Target: example.com
[+] IP Address: 93.184.216.34

[+] Port 80 OPEN
[+] Port 443 OPEN

Server: nginx
X-Powered-By: PHP/7.4

[+] Found subdomain: admin.example.com
[!] Found: http://example.com/login
```

---

## Disclaimer

This tool is intended for educational purposes only.

Only use it on systems you own or have explicit permission to test. Unauthorized scanning is illegal.

---

## Author

Mohamed Jasim

---

## Future Improvements

* Wordlist input support
* HTTPS scanning improvements
* Faster DNS resolution
* JSON output format
* Integration with external recon tools
