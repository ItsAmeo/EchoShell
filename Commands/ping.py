"""Ping command"""

import subprocess
from Commands import Command

class PingCommand(Command):
    """Test connection to a server"""
    name = "ping"
    description = "Test connection to a server"
    usage = "ping <host>"
    
    def execute(self, args):
        """Execute the ping command"""
        if not args:
            print("Usage: ping <host>")
            return
        
        host = args[0]
        try:
            result = subprocess.run(
                ["ping", "-c" if __import__('platform').system() != 'Windows' else "-n", "4", host],
                capture_output=True,
                text=True,
                timeout=10
            )
            print(result.stdout)
            if result.returncode != 0:
                print(f"Host unreachable: {host}")
        except Exception as e:
            print(f"Error pinging: {e}")
