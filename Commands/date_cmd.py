"""Date command"""

from datetime import datetime
from Commands import Command

class DateCommand(Command):
    """Display current date and time"""
    name = "date"
    description = "Display current date and time"
    usage = "date"
    
    def execute(self, args):
        """Execute the date command"""
        now = datetime.now()
        print(f"Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
