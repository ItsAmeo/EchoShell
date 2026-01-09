"""List directory command"""

import os
from Commands import Command

class LsCommand(Command):
    """List files and directories"""
    name = "ls"
    description = "List files and directories in current folder"
    usage = "ls [path]"
    
    def execute(self, args):
        """Execute the ls command"""
        try:
            path = args[0] if args else "."
            if not os.path.exists(path):
                print(f"Path not found: {path}")
                return
            
            items = os.listdir(path)
            if not items:
                print("(empty)")
                return
            
            print("\nFiles and Folders:")
            for item in sorted(items):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(f"  📁 {item}/")
                else:
                    size = os.path.getsize(full_path)
                    print(f"  📄 {item} ({size} bytes)")
            print()
        except Exception as e:
            print(f"Error listing directory: {e}")
