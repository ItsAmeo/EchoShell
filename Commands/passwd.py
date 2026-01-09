"""Password strength analyzer"""

from Commands import Command
import re

class PasswdCommand(Command):
    name = "passwd"
    description = "Password strength analyzer"
    usage = "passwd [password]"
    
    def execute(self, args):
        if not args:
            print("Usage: passwd <password>")
            return
        
        password = args[0]
        score = 0
        issues = []
        
        print(f"\n[*] Analyzing password strength...")
        
        # Length
        if len(password) >= 8:
            score += 20
        else:
            issues.append("Less than 8 characters")
        
        # Uppercase
        if re.search(r'[A-Z]', password):
            score += 20
        else:
            issues.append("No uppercase letters")
        
        # Lowercase
        if re.search(r'[a-z]', password):
            score += 20
        else:
            issues.append("No lowercase letters")
        
        # Numbers
        if re.search(r'\d', password):
            score += 20
        else:
            issues.append("No numbers")
        
        # Special chars
        if re.search(r'[!@#$%^&*]', password):
            score += 20
        else:
            issues.append("No special characters")
        
        print(f"[+] Strength: {score}%")
        if score >= 80:
            print("[+] Rating: STRONG")
        elif score >= 60:
            print("[+] Rating: MEDIUM")
        else:
            print("[+] Rating: WEAK")
        
        if issues:
            print(f"\n[!] Issues:")
            for issue in issues:
                print(f"  - {issue}")
