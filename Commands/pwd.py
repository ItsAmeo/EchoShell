"""Print working directory command"""

import os
from Commands import Command

class PwdCommand(Command):
    """Display current directory"""
    name = "pwd"
    description = "Display current working directory"
    usage = "pwd"
    
    def execute(self, args):
        """Execute the pwd command"""
        print(f"Current directory: {os.getcwd()}")
