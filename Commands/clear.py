"""Clear screen command"""

import os
from Commands import Command

class ClearCommand(Command):
    """Clear the console screen"""
    name = "clear"
    description = "Clear the console screen"
    usage = "clear"
    
    def execute(self, args):
        """Execute the clear command"""
        os.system("cls" if os.name == "nt" else "clear")
