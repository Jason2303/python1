import nmap
import requests

scanner = nmap.PortScanner()
target = "scanme.nmap.org"  # Replace with your target

print(f"Scanning {target}...")
scanner.scan(target, arguments="-Pn -T4")

for host in scanner.all_hosts():
    for proto in scanner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in ports:
            service = scanner[host][proto][port]['name']
            print(f"{host}:{port} - {service}")
            print(f"Checking for CVEs related to {service}...")
            