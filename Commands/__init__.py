"""EchoShell Commands Module - Auto-discovery and loading system"""

import os
import importlib
import inspect
from abc import ABC, abstractmethod

# Global command cache
_COMMANDS_CACHE = {}

class Command(ABC):
    """Base class for all commands"""
    name = "command"
    description = "Command description"
    usage = "usage"
    
    @abstractmethod
    def execute(self, args):
        """Execute the command with given arguments"""
        pass

def load_commands():
    """Auto-discover and load all commands from the Commands folder"""
    global _COMMANDS_CACHE
    
    # Return cached commands if available
    if _COMMANDS_CACHE:
        return _COMMANDS_CACHE
    
    commands = {}
    commands_dir = os.path.dirname(__file__)
    
    # Iterate through all Python files in Commands folder
    for filename in os.listdir(commands_dir):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = filename[:-3]  # Remove .py extension
            
            try:
                # Import the module dynamically
                module = importlib.import_module(f'Commands.{module_name}')
                
                # Find Command subclasses in the module
                for name, obj in inspect.getmembers(module):
                    if inspect.isclass(obj) and issubclass(obj, Command) and obj is not Command:
                        # Instantiate the command
                        cmd_instance = obj()
                        commands[cmd_instance.name] = cmd_instance
            except Exception as e:
                # Silently skip commands with import errors
                pass
    
    # Cache the commands
    _COMMANDS_CACHE = commands
    return commands

def get_command(name):
    """Get a specific command by name"""
    commands = load_commands()
    return commands.get(name)

def list_commands():
    """List all available commands with descriptions"""
    commands = load_commands()
    return sorted([(name, cmd.description) for name, cmd in commands.items()])

__all__ = ['Command', 'load_commands', 'get_command', 'list_commands']

"""Tree directory structure command"""
