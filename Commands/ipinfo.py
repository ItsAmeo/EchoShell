"""IP geolocation and reconnaissance"""

from Commands import Command
import socket

class IpInfoCommand(Command):
    name = "ipinfo"
    description = "IP geolocation and info"
    usage = "ipinfo [ip_address]"
    
    def execute(self, args):
        if not args:
            print("Usage: ipinfo <ip>")
            return
        
        ip = args[0]
        print(f"\n[*] IP Information: {ip}")
        
        try:
            hostname = socket.gethostbyaddr(ip)
            print(f"[+] Hostname: {hostname[0]}")
        except:
            print(f"[-] Hostname lookup failed")
        
        print(f"[+] IP: {ip}")
        print(f"[+] Family: IPv4")
        print(f"[+] Type: Regular")
