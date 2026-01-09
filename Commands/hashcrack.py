"""Hash cracking and identification"""

from Commands import Command
import hashlib

class HashCommand(Command):
    name = "hashcrack"
    description = "Hash identification and cracking"
    usage = "hashcrack [hash]"
    
    def execute(self, args):
        if not args:
            print("Usage: hashcrack <hash>")
            return
        
        hash_input = args[0]
        print(f"\n[*] Hash Analysis: {hash_input[:20]}...")
        
        # Identify hash type
        hash_len = len(hash_input)
        hash_type = "Unknown"
        
        if hash_len == 32:
            hash_type = "MD5"
        elif hash_len == 40:
            hash_type = "SHA1"
        elif hash_len == 64:
            hash_type = "SHA256"
        elif hash_len == 128:
            hash_type = "SHA512"
        
        print(f"[+] Detected Type: {hash_type}")
        
        # Try common wordlist
        wordlist = ['password', 'admin', '123456', 'qwerty', 'letmein', 'test', 'guest']
        print(f"\n[*] Trying wordlist...")
        
        for word in wordlist:
            if hash_type == "MD5":
                test_hash = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "SHA1":
                test_hash = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "SHA256":
                test_hash = hashlib.sha256(word.encode()).hexdigest()
            else:
                continue
            
            if test_hash.lower() == hash_input.lower():
                print(f"[+] CRACKED! Password: {word}")
                return
        
        print(f"[-] Password not found in wordlist")
