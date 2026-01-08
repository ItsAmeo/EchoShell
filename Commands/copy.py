"""Copy file/directory command"""

import shutil
import os
from Commands import Command

class CopyCommand(Command):
    """Copy files or directories"""
    name = "copy"
    description = "Copy a file or directory"
    usage = "copy <source> <destination>"
    
    def execute(self, args):
        """Execute the copy command"""
        if len(args) < 2:
            print("Usage: copy <source> <destination>")
            return
        
        source = args[0]
        dest = args[1]
        
        try:
            if os.path.isfile(source):
                shutil.copy2(source, dest)
                print(f"File copied: {source} -> {dest}")
            elif os.path.isdir(source):
                shutil.copytree(source, dest)
                print(f"Directory copied: {source} -> {dest}")
            else:
                print(f"Source not found: {source}")
        except Exception as e:
            print(f"Error copying: {e}")
