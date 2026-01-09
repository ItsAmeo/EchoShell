"""Network traffic analyzer"""

from Commands import Command

class SnifferCommand(Command):
    name = "sniffer"
    description = "Network packet sniffer"
    usage = "sniffer [interface] [count]"
    
    def execute(self, args):
        interface = args[0] if args else "any"
        count = int(args[1]) if len(args) > 1 else 10
        
        print(f"\n[*] Network Sniffer on {interface}")
        print(f"[*] Capturing {count} packets...\n")
        
        try:
            import subprocess
            if interface == "any":
                subprocess.call(['tcpdump', '-i', 'any', '-c', str(count)])
            else:
                subprocess.call(['tcpdump', '-i', interface, '-c', str(count)])
        except:
            print("[-] tcpdump not installed or requires root")
            print("[*] Alternative: Use Wireshark or scapy")
