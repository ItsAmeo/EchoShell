"""System information command"""

import platform
import psutil
from Commands import Command

class SysinfoCommand(Command):
    """Display system information"""
    name = "sysinfo"
    description = "Display system information (OS, CPU, RAM, etc.)"
    usage = "sysinfo"
    
    def execute(self, args):
        """Execute the sysinfo command"""
        try:
            print("\n=== System Information ===")
            print(f"OS: {platform.system()} {platform.release()}")
            print(f"Processor: {platform.processor()}")
            print(f"CPU Cores: {psutil.cpu_count()}")
            print(f"RAM: {psutil.virtual_memory().total / (1024**3):.2f} GB")
            print(f"RAM Usage: {psutil.virtual_memory().percent}%")
            print(f"Hostname: {platform.node()}")
            print()
        except Exception as e:
            print(f"Error getting system info: {e}")
