"""Calculator command"""

from Commands import Command

class CalcCommand(Command):
    """Simple calculator"""
    name = "calc"
    description = "Simple calculator (supports: +, -, *, /)"
    usage = "calc <expression>"
    
    def execute(self, args):
        """Execute the calc command"""
        if not args:
            print("Usage: calc <expression> (e.g., calc 2+2*3)")
            return
        
        expression = " ".join(args).replace(" ", "")
        try:
            result = eval(expression)
            print(f"{expression} = {result}")
        except Exception as e:
            print(f"Invalid expression: {e}")
