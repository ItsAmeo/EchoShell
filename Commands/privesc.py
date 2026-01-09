"""Privilege escalation checker"""

from Commands import Command
import os
import subprocess

class PrivescCommand(Command):
    name = "privesc"
    description = "Check for privilege escalation vectors"
    usage = "privesc"
    
    def execute(self, args):
        print("\n[*] Checking privilege escalation vectors...")
        
        if os.name == 'nt':  # Windows
            print("\n[*] Windows Privilege Escalation Checks:")
            
            # Check if admin
            try:
                is_admin = os.getuid() == 0
            except:
                is_admin = False
            
            print(f"[+] Admin: {'YES' if is_admin else 'NO'}")
            
            # Check UAC
            try:
                result = subprocess.check_output('reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA', shell=True).decode()
                print(f"[+] UAC Status: Enabled")
            except:
                print(f"[+] UAC Status: Disabled or Error")
            
            # Check AlwaysInstallElevated
            try:
                result = subprocess.check_output('reg query HKLM\\Software\\Policies\\Microsoft\\Windows\\Installer /v AlwaysInstallElevated', shell=True).decode()
                print(f"[!] AlwaysInstallElevated: VULNERABLE")
            except:
                print(f"[+] AlwaysInstallElevated: Not vulnerable")
        else:
            print("\n[*] Linux Privilege Escalation Checks:")
            print("[+] Check sudo permissions: sudo -l")
            print("[+] Check SUID binaries: find / -perm /4000 2>/dev/null")
            print("[+] Check capabilities: getcap -r / 2>/dev/null")
