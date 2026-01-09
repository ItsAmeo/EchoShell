"""Payload encoder"""

from Commands import Command
import base64
import binascii

class EncoderCommand(Command):
    name = "encoder"
    description = "Encode/decode payloads"
    usage = "encoder [action] [format] [data]"
    
    def execute(self, args):
        if len(args) < 3:
            print("Usage: encoder <action> <format> <data>")
            print("Actions: encode, decode")
            print("Formats: base64, hex, url")
            return
        
        action = args[0]
        format_ = args[1]
        data = ' '.join(args[2:])
        
        print(f"\n[*] Payload {action.upper()} ({format_.upper()})")
        
        try:
            if action == "encode":
                if format_ == "base64":
                    result = base64.b64encode(data.encode()).decode()
                elif format_ == "hex":
                    result = binascii.hexlify(data.encode()).decode()
                elif format_ == "url":
                    from urllib.parse import quote
                    result = quote(data)
                else:
                    result = "Unknown format"
            
            elif action == "decode":
                if format_ == "base64":
                    result = base64.b64decode(data).decode()
                elif format_ == "hex":
                    result = binascii.unhexlify(data).decode()
                elif format_ == "url":
                    from urllib.parse import unquote
                    result = unquote(data)
                else:
                    result = "Unknown format"
            else:
                result = "Unknown action"
            
            print(f"\n[+] Result:\n{result}")
        except Exception as e:
            print(f"[-] Error: {e}")
