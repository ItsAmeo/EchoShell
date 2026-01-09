"""SSL/TLS certificate analyzer"""

from Commands import Command
import socket
import ssl

class SslCommand(Command):
    name = "sslinfo"
    description = "Analyze SSL/TLS certificates"
    usage = "sslinfo [host] [port]"
    
    def execute(self, args):
        if not args:
            print("Usage: sslinfo <host> [port]")
            return
        
        host = args[0]
        port = int(args[1]) if len(args) > 1 else 443
        
        print(f"\n[*] Analyzing SSL/TLS: {host}:{port}...")
        
        try:
            context = ssl.create_default_context()
            with socket.create_connection((host, port)) as sock:
                with context.wrap_socket(sock, server_hostname=host) as ssock:
                    cert = ssock.getpeercert()
                    cipher = ssock.cipher()
                    version = ssock.version()
                    
                    print(f"[+] Version: {version}")
                    print(f"[+] Cipher: {cipher[0]}")
                    print(f"[+] Cipher Strength: {cipher[2]} bits")
                    
                    if 'subject' in cert:
                        subject = dict(x[0] for x in cert['subject'])
                        print(f"[+] Subject: {subject}")
        except Exception as e:
            print(f"[-] Error: {e}")
