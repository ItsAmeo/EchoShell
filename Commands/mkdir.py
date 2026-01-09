"""Make directory command"""

import os
from Commands import Command

class MkdirCommand(Command):
    """Create a new directory"""
    name = "mkdir"
    description = "Create a new directory"
    usage = "mkdir <name>"
    
    def execute(self, args):
        """Execute the mkdir command"""
        if not args:
            print("Usage: mkdir <name>")
            return
        
        folder_name = " ".join(args)
        try:
            os.makedirs(folder_name, exist_ok=True)
            print(f"Directory created: {folder_name}")
        except Exception as e:
            print(f"Error creating directory: {e}")
