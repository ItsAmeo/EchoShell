"""Echo command"""

from Commands import Command

class EchoCommand(Command):
    """Display text"""
    name = "echo"
    description = "Display text to the console"
    usage = "echo <text>"
    
    def execute(self, args):
        """Execute the echo command"""
        if not args:
            print()
            return
        
        print(" ".join(args))
