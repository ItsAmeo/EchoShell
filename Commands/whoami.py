"""Whoami command"""

import getpass
from Commands import Command

class WhoamiCommand(Command):
    """Display current user"""
    name = "whoami"
    description = "Display the current user"
    usage = "whoami"
    
    def execute(self, args):
        """Execute the whoami command"""
        user = getpass.getuser()
        print(f"Current user: {user}")
