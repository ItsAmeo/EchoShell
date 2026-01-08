"""IP command"""

import socket
from Commands import Command

class IpCommand(Command):
    """Display IP addresses"""
    name = "ip"
    description = "Display network IP addresses"
    usage = "ip"
    
    def execute(self, args):
        """Execute the ip command"""
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            print(f"Hostname: {hostname}")
            print(f"Local IP: {ip_address}")
            
            # Try to get public IP
            try:
                response = __import__('requests').get('https://api.ipify.org', timeout=3)
                print(f"Public IP: {response.text}")
            except:
                print("Public IP: (Could not retrieve)")
        except Exception as e:
            print(f"Error getting IP: {e}")
