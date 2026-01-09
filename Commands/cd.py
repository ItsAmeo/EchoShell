"""Change directory command"""

import os
from Commands import Command

class CdCommand(Command):
    """Change current directory"""
    name = "cd"
    description = "Change current directory"
    usage = "cd <path>"
    
    def execute(self, args):
        """Execute the cd command"""
        if not args:
            print("Usage: cd <path>")
            return
        
        path = " ".join(args)
        try:
            os.chdir(path)
            print(f"Changed to: {os.getcwd()}")
        except FileNotFoundError:
            print(f"Directory not found: {path}")
        except Exception as e:
            print(f"Error changing directory: {e}")
