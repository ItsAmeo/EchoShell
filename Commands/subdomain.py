"""Subdomain enumeration"""

from Commands import Command
import socket

class SubdomainCommand(Command):
    name = "subdomain"
    description = "Subdomain enumeration"
    usage = "subdomain [domain]"
    
    def execute(self, args):
        if not args:
            print("Usage: subdomain <domain>")
            return
        
        domain = args[0]
        print(f"\n[*] Subdomain Enumeration: {domain}")
        
        subdomains = [
            'admin', 'api', 'app', 'blog', 'cdn', 'dev', 'email', 'ftp',
            'git', 'mail', 'mobile', 'staging', 'test', 'vpn', 'www',
            'beta', 'support', 'store', 'shop', 'forum', 'docs'
        ]
        
        found = []
        print(f"\n[*] Testing {len(subdomains)} subdomains:\n")
        
        for sub in subdomains:
            try:
                full_domain = f"{sub}.{domain}"
                ip = socket.gethostbyname(full_domain)
                print(f"[+] {full_domain}: {ip}")
                found.append(full_domain)
            except:
                pass
        
        print(f"\n[+] Found {len(found)} subdomains")
