"""Logs command"""

import os
from Commands import Command

class LogsCommand(Command):
    """View application logs"""
    name = "logs"
    description = "View application logs"
    usage = "logs [clear|view]"
    
    LOG_FILE = "1-Output/logs.txt"
    
    def execute(self, args):
        """Execute the logs command"""
        action = args[0].lower() if args else "view"
        
        try:
            if action == "view":
                self._view_logs()
            elif action == "clear":
                self._clear_logs()
            else:
                print("Usage: logs [view|clear]")
        except Exception as e:
            print(f"Error managing logs: {e}")
    
    def _view_logs(self):
        """View logs"""
        if not os.path.exists(self.LOG_FILE):
            print("No logs available")
            return
        
        with open(self.LOG_FILE, "r") as f:
            content = f.read()
            print(content[-2000:] if len(content) > 2000 else content)
    
    def _clear_logs(self):
        """Clear logs"""
        os.makedirs(os.path.dirname(self.LOG_FILE), exist_ok=True)
        with open(self.LOG_FILE, "w") as f:
            f.write("")
        print("Logs cleared")
    
    @staticmethod
    def write_log(message):
        """Write to log file"""
        os.makedirs(os.path.dirname(LogsCommand.LOG_FILE), exist_ok=True)
        with open(LogsCommand.LOG_FILE, "a") as f:
            from datetime import datetime
            f.write(f"[{datetime.now()}] {message}\n")
