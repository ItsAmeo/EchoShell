"""Exit command for EchoShell"""

from Commands import Command

class ExitCommand(Command):
    """Exit the EchoShell application"""
    name = "exit"
    description = "Exit the EchoShell application"
    usage = "exit"
    
    def execute(self, args):
        """Execute the exit command"""
        print("Goodbye!")
        return "EXIT"  # Signal to main.py to exit
