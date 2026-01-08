"""DNS resolve command"""

import socket
from Commands import Command

class DnsCommand(Command):
    """Resolve domain names"""
    name = "dns"
    description = "Resolve a domain name to IP"
    usage = "dns <domain>"
    
    def execute(self, args):
        """Execute the dns command"""
        if not args:
            print("Usage: dns <domain>")
            return
        
        domain = args[0]
        try:
            ip = socket.gethostbyname(domain)
            print(f"{domain} -> {ip}")
        except socket.gaierror:
            print(f"Could not resolve: {domain}")
        except Exception as e:
            print(f"Error resolving DNS: {e}")
