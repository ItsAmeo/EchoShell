"""Port scanner command"""

from Commands import Command
import socket
import time

class NmapCommand(Command):
    name = "nmap"
    description = "Fast port scanner"
    usage = "nmap [host] [start_port] [end_port]"
    
    def execute(self, args):
        if len(args) < 1:
            print("Usage: nmap <host> [start] [end]")
            return
        
        host = args[0]
        start = int(args[1]) if len(args) > 1 else 1
        end = int(args[2]) if len(args) > 2 else 1024
        
        print(f"\n[*] Scanning {host} ports {start}-{end}...")
        open_ports = []
        
        for port in range(start, end + 1):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((host, port))
                if result == 0:
                    open_ports.append(port)
                    print(f"[+] Port {port}: OPEN")
                sock.close()
            except:
                pass
        
        print(f"\n[+] Found {len(open_ports)} open ports: {open_ports}")
