"""Hash file command"""

import hashlib
import os
from Commands import Command

class HashCommand(Command):
    """Calculate file hash"""
    name = "hash"
    description = "Calculate file hash (MD5, SHA256)"
    usage = "hash <filepath> [algorithm]"
    
    def execute(self, args):
        """Execute the hash command"""
        if not args:
            print("Usage: hash <filepath> [md5|sha256]")
            return
        
        filepath = args[0]
        algorithm = args[1].lower() if len(args) > 1 else "sha256"
        
        if not os.path.isfile(filepath):
            print(f"File not found: {filepath}")
            return
        
        try:
            if algorithm == "md5":
                hasher = hashlib.md5()
            elif algorithm == "sha256":
                hasher = hashlib.sha256()
            else:
                print(f"Unsupported algorithm: {algorithm}")
                return
            
            with open(filepath, "rb") as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
            
            print(f"{algorithm.upper()}: {hasher.hexdigest()}")
        except Exception as e:
            print(f"Error calculating hash: {e}")
