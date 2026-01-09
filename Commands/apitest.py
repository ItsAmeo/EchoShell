"""API testing tool"""

from Commands import Command

class ApitestCommand(Command):
    name = "apitest"
    description = "API endpoint tester"
    usage = "apitest [method] [url] [data]"
    
    def execute(self, args):
        if len(args) < 2:
            print("Usage: apitest <method> <url> [data]")
            print("Methods: GET, POST, PUT, DELETE, PATCH")
            return
        
        method = args[0].upper()
        url = args[1]
        data = args[2] if len(args) > 2 else None
        
        print(f"\n[*] API Test: {method} {url}")
        
        try:
            import requests
            
            if method == "GET":
                response = requests.get(url, timeout=5)
            elif method == "POST":
                response = requests.post(url, data=data, timeout=5)
            elif method == "PUT":
                response = requests.put(url, data=data, timeout=5)
            elif method == "DELETE":
                response = requests.delete(url, timeout=5)
            elif method == "PATCH":
                response = requests.patch(url, data=data, timeout=5)
            else:
                print(f"[-] Unknown method: {method}")
                return
            
            print(f"[+] Status Code: {response.status_code}")
            print(f"[+] Headers: {dict(response.headers)}")
            print(f"[+] Response:\n{response.text[:500]}")
        except Exception as e:
            print(f"[-] Error: {e}")
