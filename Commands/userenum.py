"""User enumeration tool"""

from Commands import Command
import os

class UserenumCommand(Command):
    name = "userenum"
    description = "User enumeration from system"
    usage = "userenum"
    
    def execute(self, args):
        print("\n[*] Enumerating system users...")
        
        if os.name == 'nt':  # Windows
            import subprocess
            try:
                result = subprocess.check_output('net user', shell=True).decode()
                users = result.split('\n')[6:-2]
                print(f"\n[+] Found {len(users)} users:\n")
                for user in users:
                    if user.strip():
                        print(f"[+] {user}")
            except:
                print("[-] Access denied")
        else:  # Linux
            try:
                with open('/etc/passwd', 'r') as f:
                    for line in f:
                        parts = line.split(':')
                        if parts:
                            print(f"[+] {parts[0]} (UID: {parts[2]})")
            except:
                print("[-] Permission denied")
