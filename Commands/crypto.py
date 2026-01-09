"""Cryptography and Encryption Tools"""

from Commands import Command
import hashlib
import hmac

class CryptoCommand(Command):
    name = "crypto"
    description = "Cryptographic operations"
    usage = "crypto [action] [data]"
    
    def execute(self, args):
        if len(args) < 2:
            print("[!] Usage: crypto <action> <data>")
            print("Actions: hash, hmac, encrypt, decrypt")
            return
        
        action = args[0]
        data = ' '.join(args[1:])
        
        print(f"\n[*] Cryptographic Operations")
        
        if action == "hash":
            print(f"[+] Input: {data}")
            print(f"  [+] MD5: {hashlib.md5(data.encode()).hexdigest()}")
            print(f"  [+] SHA1: {hashlib.sha1(data.encode()).hexdigest()}")
            print(f"  [+] SHA256: {hashlib.sha256(data.encode()).hexdigest()}")
            print(f"  [+] SHA512: {hashlib.sha512(data.encode()).hexdigest()}")
        
        elif action == "hmac":
            secret = "SecretKey123"
            print(f"[+] HMAC Calculation:")
            print(f"  [+] Data: {data}")
            print(f"  [+] Key: {secret}")
            hmac_result = hmac.new(secret.encode(), data.encode(), hashlib.sha256).hexdigest()
            print(f"  [+] HMAC-SHA256: {hmac_result}")
        
        elif action == "encrypt":
            print("[+] Encryption (Educational):")
            print("  [!] Use industry-standard tools like:")
            print("      - openssl enc -aes-256-cbc -in file.txt -out file.enc")
            print("      - GnuPG for PGP encryption")
            print("      - 7-Zip with AES encryption")
        
        elif action == "decrypt":
            print("[+] Decryption (Educational):")
            print("  [!] Use corresponding decryption tools")
