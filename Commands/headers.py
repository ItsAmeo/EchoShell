"""HTTP header analyzer"""

from Commands import Command
import socket

class HeadersCommand(Command):
    name = "headers"
    description = "Analyze HTTP headers"
    usage = "headers [host] [port]"
    
    def execute(self, args):
        if not args:
            print("Usage: headers <host> [port]")
            return
        
        host = args[0]
        port = int(args[1]) if len(args) > 1 else 80
        
        print(f"\n[*] Fetching headers from {host}:{port}...")
        
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
            sock.sendall(request.encode())
            
            response = b""
            while True:
                data = sock.recv(4096)
                if not data:
                    break
                response += data
            
            sock.close()
            
            headers = response.decode('utf-8', errors='ignore').split('\r\n\r\n')[0]
            print(f"\n[+] Headers:\n{headers}")
        except Exception as e:
            print(f"[-] Error: {e}")
