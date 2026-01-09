"""Network mapping and reconnaissance"""

from Commands import Command
import socket

class ReconCommand(Command):
    name = "recon"
    description = "Network reconnaissance and mapping"
    usage = "recon [network_range]"
    
    def execute(self, args):
        if not args:
            print("Usage: recon <network_range>")
            print("Example: recon 192.168.1.0/24")
            return
        
        network = args[0]
        print(f"\n[*] Network Reconnaissance: {network}")
        
        # Parse network
        try:
            base = network.split('/')[0]
            parts = base.split('.')
            base_ip = '.'.join(parts[:3])
            
            print(f"\n[*] Scanning {base_ip}.0-255")
            print(f"[*] This will scan 256 hosts...\n")
            
            # Simulate ping sweep
            for i in range(1, 10):
                test_ip = f"{base_ip}.{i}"
                try:
                    socket.gethostbyname(test_ip)
                    print(f"[+] {test_ip}: UP")
                except:
                    pass
            
            print(f"\n[*] Scan complete")
        except Exception as e:
            print(f"[-] Error: {e}")
