"""Curl command"""

from Commands import Command

class CurlCommand(Command):
    """Download content from URL"""
    name = "curl"
    description = "Download and display content from a URL"
    usage = "curl <url>"
    
    def execute(self, args):
        """Execute the curl command"""
        if not args:
            print("Usage: curl <url>")
            return
        
        url = args[0]
        try:
            import requests
            response = requests.get(url, timeout=10)
            print(response.text[:1000])
            if len(response.text) > 1000:
                print(f"\n... (truncated, {len(response.text)} total bytes)")
        except Exception as e:
            print(f"Error fetching URL: {e}")
