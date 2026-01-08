"""Commands module for EchoShell"""

import os
import importlib
import inspect
import sys

class Command:
    """Base class for all commands"""
    name = None
    description = "No description"
    usage = ""
    
    def execute(self, args):
        """Execute the command. Should be overridden by subclasses."""
        raise NotImplementedError

# Command registry for faster lookups
_COMMAND_REGISTRY = {}
_REGISTRY_LOADED = False

def load_commands():
    """Dynamically load all commands from this directory (cached)"""
    global _COMMAND_REGISTRY, _REGISTRY_LOADED
    
    if _REGISTRY_LOADED:
        return _COMMAND_REGISTRY
    
    commands = {}
    commands_dir = os.path.dirname(__file__)
    
    # Get all command files
    command_files = [f[:-3] for f in os.listdir(commands_dir) 
                     if f.endswith('.py') and f != '__init__.py']
    
    for module_name in command_files:
        try:
            # Use importlib for faster loading
            module = importlib.import_module(f'Commands.{module_name}')
            
            # Find Command subclass (usually only one per file)
            for name in dir(module):
                obj = getattr(module, name)
                if (inspect.isclass(obj) and 
                    issubclass(obj, Command) and 
                    obj != Command and
                    hasattr(obj, 'name') and 
                    obj.name):
                    try:
                        cmd_instance = obj()
                        commands[cmd_instance.name] = cmd_instance
                        break  # Move to next module after finding first Command
                    except Exception:
                        pass
        except Exception:
            pass  # Silently skip failed imports
    
    _COMMAND_REGISTRY = commands
    _REGISTRY_LOADED = True
    return commands

