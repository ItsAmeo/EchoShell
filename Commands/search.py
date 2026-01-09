"""Search files command"""

import os
from Commands import Command

class SearchCommand(Command):
    """Search for files"""
    name = "search"
    description = "Search for files by name"
    usage = "search <filename> [path]"
    
    def execute(self, args):
        """Execute the search command"""
        if not args:
            print("Usage: search <filename> [path]")
            return
        
        filename = args[0]
        search_path = args[1] if len(args) > 1 else "."
        
        if not os.path.exists(search_path):
            print(f"Path not found: {search_path}")
            return
        
        matches = []
        try:
            for root, dirs, files in os.walk(search_path):
                for file in files:
                    if filename.lower() in file.lower():
                        matches.append(os.path.join(root, file))
            
            if matches:
                print(f"\nFound {len(matches)} match(es):")
                for match in matches[:50]:
                    print(f"  {match}")
                if len(matches) > 50:
                    print(f"  ... and {len(matches) - 50} more")
            else:
                print(f"No files found matching: {filename}")
        except Exception as e:
            print(f"Error searching: {e}")
