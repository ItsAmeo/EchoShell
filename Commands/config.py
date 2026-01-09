"""Secure Configuration Management"""

from Commands import Command

class ConfigCommand(Command):
    name = "config"
    description = "Secure configuration and hardening"
    usage = "config [system]"
    
    def execute(self, args):
        system = args[0] if args else "windows"
        
        print(f"\n[*] Secure Configuration Management - {system}")
        
        if system == "windows":
            print("[+] Windows Hardening Checklist:")
            checks = [
                ("Disable unnecessary services", "WinRM, Telnet, SNMP"),
                ("Configure Windows Firewall", "Block all inbound by default"),
                ("Enable Windows Defender", "Real-time protection enabled"),
                ("Apply security updates", "Monthly updates scheduled"),
                ("Configure UAC", "Highest level enabled"),
                ("Enable Audit Logging", "Monitor all events"),
                ("Configure Local Policies", "Password policy enforced"),
                ("Disable USB drives", "Block unauthorized storage")
            ]
            
            for check, detail in checks:
                print(f"  [+] {check}")
                print(f"      -> {detail}")
        
        elif system == "linux":
            print("[+] Linux Hardening Checklist:")
            checks = [
                ("File Permissions", "chmod 600 /etc/shadow"),
                ("SSH Hardening", "Disable root login, change port"),
                ("Firewall (iptables)", "Block all inbound by default"),
                ("SELinux", "Enable enforcing mode"),
                ("System Updates", "apt-get update && apt-get upgrade"),
                ("Remove unnecessary packages", "apt-get remove telnet"),
                ("Configure sudo", "Require password, log commands"),
                ("Setup monitoring", "Install aide, configure aide")
            ]
            
            for check, command in checks:
                print(f"  [+] {check}")
                print(f"      $ {command}")
        
        elif system == "network":
            print("[+] Network Hardening:")
            print("  [+] VPN Configuration")
            print("      - Force VPN for remote access")
            print("      - Use IPSec or SSL/TLS")
            print("  [+] Network Segmentation")
            print("      - Separate VLAN for servers")
            print("      - DMZ for public-facing services")
            print("  [+] Access Control Lists")
            print("      - Whitelist required traffic")
            print("      - Block all by default")
