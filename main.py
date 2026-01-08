#!/usr/bin/env python3
"""
EchoShell - A CLI interface in Python
"""

# Standard Library
import socket
import os
import sys
import platform
import subprocess
import getpass
import shutil
from datetime import datetime
import json
import hashlib
import inspect
import importlib
import psutil

# Third Party
try:
    import requests
    from colorama import init, Fore, Style
except ImportError:
    print("Installing required packages...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "colorama", "psutil"])
    import requests
    from colorama import init, Fore, Style

# Initialize colorama for cross-platform color support
init(autoreset=True)

from Commands import load_commands

# ============================================================================
# AUTHENTICATION TOKENS - Access Control
# ============================================================================
VALID_TOKENS = {
    "=tQqrK4.;):1,Pk6[o6TqYk#FrZj2:'wVcU7S|m0LW*[I(xCSXS4dQXme0IMY@.k",  # Admin Token
    "nX9pL2@mQ$vT#rE&yF*jG(kH)lW,zA.bC[dE]fG{hI|jK:lM;nO'pQ-qR=sT+uV/wX", # Token 2
}

# Discord Webhook URL
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1458713591128784989/w35j4P3BpUxsypStD3m4U5sUgI4fRyP5KObCY59bq30pPYFxFUOmKw_cyx4P5tMqjFGw"

# Banner lines with gradient colors (Red -> Orange -> Yellow)
BANNER_LINES = [
    "▓█████  ▄████▄   ██░ ██  ▒█████       ██████  ██░ ██ ▓█████  ██▓     ██▓    ",
    "▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒   ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ",
    "▒███   ▒▓█    ▄ ▒██▀▀██░▒██░  ██▒   ░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    ",
    "▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░     ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    ",
    "░▒████▒▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░   ▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒",
    "░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░",
    " ░ ░  ░  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░    ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░",
    "   ░   ░         ░  ░░ ░░ ░ ░ ▒     ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   ",
    "   ░  ░░ ░       ░  ░  ░    ░ ░           ░   ░  ░  ░   ░  ░    ░  ░    ░  ░",
    "       ░                                                                    ",
]

# Banner lines with gradient colors (Red -> Orange -> Yellow)
BANNER_LINES = [
    "▓█████  ▄████▄   ██░ ██  ▒█████       ██████  ██░ ██ ▓█████  ██▓     ██▓    ",
    "▓█   ▀ ▒██▀ ▀█  ▓██░ ██▒▒██▒  ██▒   ▒██    ▒ ▓██░ ██▒▓█   ▀ ▓██▒    ▓██▒    ",
    "▒███   ▒▓█    ▄ ▒██▀▀██░▒██░  ██▒   ░ ▓██▄   ▒██▀▀██░▒███   ▒██░    ▒██░    ",
    "▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█ ░██ ▒██   ██░     ▒   ██▒░▓█ ░██ ▒▓█  ▄ ▒██░    ▒██░    ",
    "░▒████▒▒ ▓███▀ ░░▓█▒░██▓░ ████▓▒░   ▒██████▒▒░▓█▒░██▓░▒████▒░██████▒░██████▒",
    "░░ ▒░ ░░ ░▒ ▒  ░ ▒ ░░▒░▒░ ▒░▒░▒░    ▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░░ ▒░ ░░ ▒░▓  ░░ ▒░▓  ░",
    " ░ ░  ░  ░  ▒    ▒ ░▒░ ░  ░ ▒ ▒░    ░ ░▒  ░ ░ ▒ ░▒░ ░ ░ ░  ░░ ░ ▒  ░░ ░ ▒  ░",
    "   ░   ░         ░  ░░ ░░ ░ ░ ▒     ░  ░  ░   ░  ░░ ░   ░     ░ ░     ░ ░   ",
    "   ░  ░░ ░       ░  ░  ░    ░ ░           ░   ░  ░  ░   ░  ░    ░  ░    ░  ░",
    "       ░                                                                    ",
]

def interpolate_color(start_rgb, end_rgb, factor):
    """Interpolate between two RGB colors"""
    r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * factor)
    g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * factor)
    b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * factor)
    return (r, g, b)

def rgb_to_ansi(r, g, b):
    """Convert RGB color to ANSI escape code"""
    return f"\033[38;2;{r};{g};{b}m"

def get_colored_banner():
    """Generate banner with smooth gradient colors (Red -> Orange -> Yellow)"""
    # Define color gradient points
    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)
    
    banner = "\n"
    num_lines = len(BANNER_LINES)
    
    for i, line in enumerate(BANNER_LINES):
        # Calculate gradient factor (0 to 1)
        factor = i / max(num_lines - 1, 1)
        
        # Create smooth gradient: Red -> Orange -> Yellow
        if factor < 0.5:
            # Red to Orange
            t = factor * 2
            color = interpolate_color(red, orange, t)
        else:
            # Orange to Yellow
            t = (factor - 0.5) * 2
            color = interpolate_color(orange, yellow, t)
        
        color_code = rgb_to_ansi(color[0], color[1], color[2])
        reset_code = "\033[0m"
        banner += f"{color_code}{line}{reset_code}\n"
    
    banner += "\n"
    return banner

def send_webhook_notification():
    """Send a notification to Discord webhook when app opens (non-blocking)"""
    import threading
    
    def send_async():
        try:
            pc_name = socket.gethostname()
            message = {
                "content": f"🚀 EchoShell opened on: **{pc_name}**"
            }
            requests.post(DISCORD_WEBHOOK, json=message, timeout=3)
        except Exception:
            pass  # Silently fail, don't block the app
    
    # Send webhook in background thread
    thread = threading.Thread(target=send_async, daemon=True)
    thread.start()

# Global cache for commands
_COMMANDS_CACHE = None

def get_settings_path():
    """Get the path to Settings.json"""
    config_dir = os.path.join(os.path.dirname(__file__), 'Config')
    os.makedirs(config_dir, exist_ok=True)
    return os.path.join(config_dir, 'Settings.json')

def load_settings():
    """Load settings from Settings.json"""
    settings_path = get_settings_path()
    default_settings = {
        "autoauth": None,
        "autoauth_enabled": True,
        "theme": "default",
        "notifications_enabled": True
    }
    
    if os.path.exists(settings_path):
        try:
            with open(settings_path, 'r') as f:
                loaded = json.load(f)
                default_settings.update(loaded)
        except:
            pass
    
    return default_settings

def save_settings(settings):
    """Save settings to Settings.json"""
    settings_path = get_settings_path()
    try:
        with open(settings_path, 'w') as f:
            json.dump(settings, f, indent=2)
    except Exception as e:
        print(f"Warning: Could not save settings: {e}")

def get_commands():
    """Get commands (cached after first load)"""
    global _COMMANDS_CACHE
    if _COMMANDS_CACHE is None:
        _COMMANDS_CACHE = load_commands()
    return _COMMANDS_CACHE

def authenticate():
    """Authenticate user with token before starting EchoShell"""
    settings = load_settings()
    
    # Try auto-auth first (only if enabled)
    if settings.get("autoauth_enabled", True) and settings.get("autoauth"):
        if settings["autoauth"] in VALID_TOKENS:
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
    
    # Manual authentication
    print("\n" + "="*70)
    print(Fore.CYAN + "🔐 EchoShell Authentication Required")
    print("="*70 + Style.RESET_ALL)
    print()
    
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        attempts += 1
        
        # Get token input (visible)
        token_input = input(
            Fore.YELLOW + f"🔑 Enter access token ({max_attempts - attempts + 1} attempts left): " + Style.RESET_ALL
        )
        
        if token_input in VALID_TOKENS:
            # Save token to settings
            settings["autoauth"] = token_input
            save_settings(settings)
            
            # Clear screen after successful authentication
            os.system('cls' if os.name == 'nt' else 'clear')
            return True
        else:
            remaining = max_attempts - attempts
            if remaining > 0:
                print(Fore.RED + f"❌ Invalid token! {remaining} attempt{'s' if remaining > 1 else ''} remaining." + Style.RESET_ALL)
                print()
            else:
                print(Fore.RED + "❌ Authentication failed! Access denied." + Style.RESET_ALL)
                print()
    
    return False

def main():
    """Main entry point for EchoShell"""
    # Authenticate first
    if not authenticate():
        print(Fore.RED + "🚫 Access denied. Exiting EchoShell." + Style.RESET_ALL)
        sys.exit(1)
    
    print(get_colored_banner())
    
    # Send webhook notification asynchronously
    send_webhook_notification()
    
    # Lazy load commands on first input
    commands = None
    
    # Keep the CLI running
    while True:
        try:
            user_input = input("EchoShell> ").strip()
            if not user_input:
                continue
            
            # Load commands on first use (lazy loading)
            if commands is None:
                commands = get_commands()
            
            # Parse command and arguments
            parts = user_input.split()
            cmd_name = parts[0].lower()
            args = parts[1:] if len(parts) > 1 else []
            
            # Check if command exists
            if cmd_name in commands:
                result = commands[cmd_name].execute(args)
                if result == "EXIT":
                    break
            elif cmd_name in ['?', 'help']:
                print("\nAvailable commands:")
                for name, cmd in sorted(commands.items()):
                    print(f"  {cmd.usage:<30} - {cmd.description}")
                print()
            else:
                print(f"Unknown command: {cmd_name}. Type 'help' for available commands.")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
            
if __name__ == "__main__":
    main()
