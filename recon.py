import socket
import requests
import threading
from queue import Queue
from urllib.parse import urlparse
import argparse

parser = argparse.ArgumentParser(description="Advanced Web Recon Tool")
parser.add_argument("target", help="Target URL (e.g., http://example.com)")
parser.add_argument("-t", "--threads", type=int, default=50, help="Number of threads")
parser.add_argument("-o", "--output", help="Save output to file")

args = parser.parse_args()

target = args.target
threads = args.threads
output_file = args.output

parsed = urlparse(target)
domain = parsed.netloc

results = []

def log(data):
    print(data)
    results.append(data)

def resolve_ip():
    try:
        ip = socket.gethostbyname(domain)
        log(f"[+] IP Address: {ip}")
    except:
        log("[-] Could not resolve domain")

def port_scan():
    log("\n[+] Scanning common ports...")
    ports = [21,22,25,53,80,110,143,443,3306,8080]
    queue = Queue()

    def scan():
        while not queue.empty():
            port = queue.get()
            try:
                sock = socket.socket()
                sock.settimeout(0.5)
                if sock.connect_ex((domain, port)) == 0:
                    log(f"[+] Port {port} OPEN")
                sock.close()
            except:
                pass
            queue.task_done()

    for port in ports:
        queue.put(port)

    for _ in range(threads):
        threading.Thread(target=scan, daemon=True).start()

    queue.join()

def headers_check():
    log("\n[+] Fetching headers...")
    try:
        r = requests.get(target, timeout=3)

        for k, v in r.headers.items():
            log(f"{k}: {v}")

        log("\n[+] Technologies:")
        log(f"Server: {r.headers.get('Server', 'Unknown')}")
        log(f"X-Powered-By: {r.headers.get('X-Powered-By', 'Unknown')}")

    except:
        log("[-] Failed to fetch headers")

def subdomain_enum():
    log("\n[+] Enumerating subdomains...")
    subs = ["www", "mail", "dev", "test", "admin"]

    for sub in subs:
        subdomain = f"{sub}.{domain}"
        try:
            socket.gethostbyname(subdomain)
            log(f"[+] Found subdomain: {subdomain}")
        except:
            pass

def dir_bruteforce():
    log("\n[+] Directory brute force...")
    paths = ["admin", "login", "dashboard", "uploads", "backup"]

    queue = Queue()

    def scan():
        while not queue.empty():
            path = queue.get()
            url = f"{target}/{path}"
            try:
                r = requests.get(url, timeout=3)
                if r.status_code == 200:
                    log(f"[!] Found: {url}")
            except:
                pass
            queue.task_done()

    for path in paths:
        queue.put(path)

    for _ in range(threads):
        threading.Thread(target=scan, daemon=True).start()

    queue.join()

def main():
    log(f"\n[+] Target: {domain}")

    resolve_ip()
    port_scan()
    headers_check()
    subdomain_enum()
    dir_bruteforce()

    log("\n[+] Recon Completed!")

    if output_file:
        with open(output_file, "w") as f:
            for line in results:
                f.write(line + "\n")

if __name__ == "__main__":
    main()