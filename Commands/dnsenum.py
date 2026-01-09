"""DNS enumeration command"""

from Commands import Command
import socket

class DnsEnumCommand(Command):
    name = "dnsenum"
    description = "DNS enumeration and lookup"
    usage = "dnsenum [domain]"
    
    def execute(self, args):
        if not args:
            print("Usage: dnsenum <domain>")
            return
        
        domain = args[0]
        print(f"\n[*] DNS Enumeration: {domain}")
        
        try:
            # A record
            a_record = socket.gethostbyname(domain)
            print(f"[+] A Record: {a_record}")
        except:
            print(f"[-] A Record not found")
        
        # Common subdomains
        subdomains = ['www', 'mail', 'ftp', 'admin', 'api', 'test', 'dev', 'staging']
        print(f"\n[*] Checking subdomains...")
        for sub in subdomains:
            try:
                ip = socket.gethostbyname(f"{sub}.{domain}")
                print(f"[+] {sub}.{domain}: {ip}")
            except:
                pass
