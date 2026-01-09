"""Active Directory reconnaissance"""

from Commands import Command
import subprocess

class AdCommand(Command):
    name = "ad"
    description = "Active Directory reconnaissance"
    usage = "ad [action]"
    
    def execute(self, args):
        action = args[0] if args else "info"
        
        print(f"\n[*] Active Directory Reconnaissance")
        
        if action == "info":
            try:
                result = subprocess.check_output('wmic computersystem get domain', shell=True).decode()
                print(f"[+] Domain:\n{result}")
            except:
                print("[-] Not on domain or error occurred")
        
        elif action == "users":
            try:
                result = subprocess.check_output('net group \"Domain Users\" /domain', shell=True).decode()
                print(f"[+] Domain Users:\n{result}")
            except:
                print("[-] Error retrieving users")
        
        elif action == "computers":
            try:
                result = subprocess.check_output('net group \"Domain Computers\" /domain', shell=True).decode()
                print(f"[+] Domain Computers:\n{result}")
            except:
                print("[-] Error retrieving computers")
        
        elif action == "admins":
            try:
                result = subprocess.check_output('net group \"Domain Admins\" /domain', shell=True).decode()
                print(f"[+] Domain Admins:\n{result}")
            except:
                print("[-] Error retrieving admins")
