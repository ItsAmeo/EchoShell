"""Tree directory structure command"""

import os
from Commands import Command

class TreeCommand(Command):
    """Display directory tree"""
    name = "tree"
    description = "Display directory structure as a tree"
    usage = "tree [path] [depth]"
    
    def execute(self, args):
        """Execute the tree command"""
        path = args[0] if args else "."
        max_depth = int(args[1]) if len(args) > 1 else 3
        
        if not os.path.exists(path):
            print(f"Path not found: {path}")
            return
        
        self._print_tree(path, "", 0, max_depth)
    
    def _print_tree(self, path, prefix, depth, max_depth):
        """Recursively print directory tree"""
        if depth > max_depth:
            return
        
        try:
            items = sorted(os.listdir(path))
            dirs = [i for i in items if os.path.isdir(os.path.join(path, i))]
            files = [i for i in items if os.path.isfile(os.path.join(path, i))]
            
            for f in files:
                print(f"{prefix}├── {f}")
            
            for i, d in enumerate(dirs):
                is_last = (i == len(dirs) - 1)
                print(f"{prefix}├── {d}/")
                new_prefix = prefix + ("│   " if not is_last else "    ")
                self._print_tree(os.path.join(path, d), new_prefix, depth + 1, max_depth)
        except PermissionError:
            print(f"{prefix}(Permission denied)")
