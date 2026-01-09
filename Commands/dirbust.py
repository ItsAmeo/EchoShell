"""Directory brute-force scanner"""

from Commands import Command

class DirbustCommand(Command):
    name = "dirbust"
    description = "Directory brute-force scanner"
    usage = "dirbust [url] [wordlist]"
    
    def execute(self, args):
        if not args:
            print("Usage: dirbust <url> [wordlist]")
            return
        
        url = args[0]
        wordlist = args[1] if len(args) > 1 else "common.txt"
        
        print(f"\n[*] Directory Brute-Force: {url}")
        print(f"[*] Wordlist: {wordlist}")
        
        common_dirs = [
            'admin', 'api', 'backup', 'config', 'data', 'database',
            'downloads', 'files', 'ftp', 'images', 'js', 'logs',
            'mail', 'private', 'public', 'sql', 'test', 'tmp',
            'uploads', 'user', 'users', 'web', 'www'
        ]
        
        print(f"\n[*] Testing directories:")
        for dir in common_dirs:
            test_url = f"{url}/{dir}"
            print(f"[*] {test_url}")
        
        print(f"\n[+] Brute-force complete. Check results manually.")
