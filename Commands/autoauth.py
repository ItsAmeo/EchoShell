"""Autoauth command - Enable/Disable automatic authentication"""

import os
import json
from Commands import Command

class AutoauthCommand(Command):
    """Manage automatic authentication"""
    name = "autoauth"
    description = "Enable/Disable automatic authentication with saved token"
    usage = "autoauth enable|disable|status"
    
    def execute(self, args):
        """Execute the autoauth command"""
        if not args:
            print("\n❌ Usage: autoauth enable|disable|status")
            return
        
        action = args[0].lower()
        settings_path = self._get_settings_path()
        settings = self._load_settings(settings_path)
        
        if action == "enable":
            if settings.get("autoauth"):
                settings["autoauth_enabled"] = True
                self._save_settings(settings_path, settings)
                print("\n✅ Auto-auth enabled! Next time you'll be automatically logged in.")
            else:
                print("\n❌ No token saved. Please authenticate manually first.")
            
        elif action == "disable":
            settings["autoauth_enabled"] = False
            self._save_settings(settings_path, settings)
            print("\n✅ Auto-auth disabled! You'll need to enter token on next startup.")
            
        elif action == "status":
            is_enabled = settings.get("autoauth_enabled", True)
            has_token = bool(settings.get("autoauth"))
            status = "🟢 ENABLED" if is_enabled else "🔴 DISABLED"
            token_status = "✓ Token saved" if has_token else "✗ No token"
            print(f"\n📊 Auto-auth Status: {status}")
            print(f"📝 {token_status}")
            
        else:
            print(f"\n❌ Unknown action: {action}")
            print("Usage: autoauth enable|disable|status")
        
        print()
    
    def _get_settings_path(self):
        """Get path to Settings.json"""
        config_dir = os.path.join(os.path.dirname(__file__), '..', 'Config')
        os.makedirs(config_dir, exist_ok=True)
        return os.path.join(config_dir, 'Settings.json')
    
    def _load_settings(self, path):
        """Load settings from file"""
        default = {
            "autoauth": None,
            "autoauth_enabled": True,
            "theme": "default",
            "notifications_enabled": True
        }
        
        if os.path.exists(path):
            try:
                with open(path, 'r') as f:
                    loaded = json.load(f)
                    default.update(loaded)
            except:
                pass
        
        return default
    
    def _save_settings(self, path, settings):
        """Save settings to file"""
        try:
            with open(path, 'w') as f:
                json.dump(settings, f, indent=2)
        except Exception as e:
            print(f"❌ Error saving settings: {e}")
