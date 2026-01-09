"""Wordlist generator"""

from Commands import Command

class WordgenCommand(Command):
    name = "wordgen"
    description = "Generate custom wordlists"
    usage = "wordgen [min_len] [max_len] [charset]"
    
    def execute(self, args):
        min_len = int(args[0]) if args else 3
        max_len = int(args[1]) if len(args) > 1 else 6
        charset = args[2] if len(args) > 2 else "common"
        
        charsets = {
            "lower": "abcdefghijklmnopqrstuvwxyz",
            "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
            "digits": "0123456789",
            "special": "!@#$%^&*",
            "common": "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        }
        
        chars = charsets.get(charset, charsets["common"])
        
        print(f"\n[*] Generating wordlist...")
        print(f"[*] Length: {min_len}-{max_len}, Charset: {charset}")
        
        wordlist = []
        
        # Generate common passwords
        common = ['password', 'admin', 'letmein', 'welcome', 'monkey', '123456', 'qwerty', 'dragon']
        wordlist.extend(common)
        
        # Generate combinations
        count = 0
        import itertools
        for length in range(min_len, min(max_len + 1, 4)):
            for combo in itertools.combinations_with_replacement(chars, length):
                wordlist.append(''.join(combo))
                count += 1
                if count > 1000:  # Limit output
                    break
            if count > 1000:
                break
        
        print(f"[+] Generated {len(wordlist)} passwords")
        
        # Save to file
        try:
            with open('wordlist.txt', 'w') as f:
                f.write('\n'.join(wordlist))
            print(f"[+] Saved to wordlist.txt")
        except:
            for word in wordlist[:20]:
                print(f"[+] {word}")
            print(f"... and {len(wordlist)-20} more")
