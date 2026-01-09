"""Built-in help command for EchoShell"""

from Commands import Command
import os

class HelpCommand(Command):
    name = "help"
    description = "Display help documentation"
    usage = "help [command]"
    
    def execute(self, args):
        help_file = os.path.join(os.path.dirname(__file__), '..', 'help.txt')
        
        if not os.path.exists(help_file):
            print("[-] Help file not found")
            return
        
        if args:
            # Search for specific command
            search_term = args[0].lower()
            with open(help_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Search for command sections
            if f"[{len(search_term)}] {search_term.upper()}" in content or f"] {search_term.upper()}\n" in content:
                lines = content.split('\n')
                found = False
                for i, line in enumerate(lines):
                    if search_term.upper() in line and ('Description:' in lines[i+1] if i+1 < len(lines) else False):
                        found = True
                        for j in range(i, min(i + 12, len(lines))):
                            print(lines[j])
                        break
                
                if not found:
                    print(f"[*] Help file found. Run 'help' without arguments to view full documentation")
            else:
                print(f"[!] No help found for command: {search_term}")
                print("[*] Type 'help' to view all available commands")
        else:
            # Display full help
            with open(help_file, 'r', encoding='utf-8') as f:
                content = f.read()
            print(content)
