"""Settings command"""

import json
import os
from Commands import Command

class SettingsCommand(Command):
    """Manage application settings"""
    name = "settings"
    description = "Manage application settings"
    usage = "settings [get|set|list]"
    
    CONFIG_FILE = "Config/settings.json"
    
    def execute(self, args):
        """Execute the settings command"""
        if not args:
            print("Usage: settings [get|set|list] [key] [value]")
            return
        
        action = args[0].lower()
        
        try:
            if action == "list":
                self._list_settings()
            elif action == "get":
                if len(args) < 2:
                    print("Usage: settings get <key>")
                    return
                self._get_setting(args[1])
            elif action == "set":
                if len(args) < 3:
                    print("Usage: settings set <key> <value>")
                    return
                self._set_setting(args[1], " ".join(args[2:]))
            else:
                print("Unknown action. Use: get, set, list")
        except Exception as e:
            print(f"Error managing settings: {e}")
    
    def _load_settings(self):
        """Load settings from file"""
        if os.path.exists(self.CONFIG_FILE):
            with open(self.CONFIG_FILE, "r") as f:
                return json.load(f)
        return {}
    
    def _save_settings(self, settings):
        """Save settings to file"""
        os.makedirs(os.path.dirname(self.CONFIG_FILE), exist_ok=True)
        with open(self.CONFIG_FILE, "w") as f:
            json.dump(settings, f, indent=2)
    
    def _list_settings(self):
        """List all settings"""
        settings = self._load_settings()
        if not settings:
            print("No settings configured")
            return
        for key, value in settings.items():
            print(f"  {key}: {value}")
    
    def _get_setting(self, key):
        """Get a setting value"""
        settings = self._load_settings()
        if key in settings:
            print(f"{key}: {settings[key]}")
        else:
            print(f"Setting not found: {key}")
    
    def _set_setting(self, key, value):
        """Set a setting value"""
        settings = self._load_settings()
        settings[key] = value
        self._save_settings(settings)
        print(f"Setting saved: {key} = {value}")
