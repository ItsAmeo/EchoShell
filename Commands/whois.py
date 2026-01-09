"""WHOIS lookup"""

from Commands import Command
import socket

class WhoisCommand(Command):
    name = "whois"
    description = "WHOIS domain information"
    usage = "whois [domain]"
    
    def execute(self, args):
        if not args:
            print("Usage: whois <domain>")
            return
        
        domain = args[0]
        print(f"\n[*] WHOIS Lookup: {domain}")
        
        try:
            # Try to get IP
            ip = socket.gethostbyname(domain)
            print(f"[+] IP Address: {ip}")
        except:
            print(f"[-] Domain not found")
            return
        
        print(f"[+] Domain: {domain}")
        print(f"[+] Status: Active")
        print(f"[+] Type: Domain")
        
        # Mock WHOIS data
        print(f"\n[*] Note: For real WHOIS data, use:")
        print(f"whois {domain}")
