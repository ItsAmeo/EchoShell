"""Remove file/directory command"""

import os
import shutil
from Commands import Command

class RmCommand(Command):
    """Delete a file or directory"""
    name = "rm"
    description = "Delete a file or directory"
    usage = "rm <path>"
    
    def execute(self, args):
        """Execute the rm command"""
        if not args:
            print("Usage: rm <path>")
            return
        
        path = " ".join(args)
        try:
            if os.path.isfile(path):
                os.remove(path)
                print(f"File deleted: {path}")
            elif os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Directory deleted: {path}")
            else:
                print(f"Path not found: {path}")
        except Exception as e:
            print(f"Error deleting: {e}")
