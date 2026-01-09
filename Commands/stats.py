"""Statistics command"""

import json
import os
from datetime import datetime
from Commands import Command

class StatsCommand(Command):
    """View application statistics"""
    name = "stats"
    description = "View application usage statistics"
    usage = "stats [reset]"
    
    STATS_FILE = "1-Output/stats.json"
    
    def execute(self, args):
        """Execute the stats command"""
        if args and args[0].lower() == "reset":
            self._reset_stats()
        else:
            self._view_stats()
    
    def _view_stats(self):
        """View statistics"""
        stats = self._load_stats()
        print("\n=== Application Statistics ===")
        for key, value in stats.items():
            print(f"  {key}: {value}")
        print()
    
    def _reset_stats(self):
        """Reset statistics"""
        self._save_stats({
            "commands_executed": 0,
            "start_time": str(datetime.now()),
            "last_reset": str(datetime.now())
        })
        print("Statistics reset")
    
    def _load_stats(self):
        """Load statistics"""
        if os.path.exists(self.STATS_FILE):
            with open(self.STATS_FILE, "r") as f:
                return json.load(f)
        return {
            "commands_executed": 0,
            "start_time": str(datetime.now()),
            "last_reset": str(datetime.now())
        }
    
    def _save_stats(self, stats):
        """Save statistics"""
        os.makedirs(os.path.dirname(self.STATS_FILE), exist_ok=True)
        with open(self.STATS_FILE, "w") as f:
            json.dump(stats, f, indent=2)
    
    @staticmethod
    def increment_command_count():
        """Increment command count"""
        stats_file = StatsCommand.STATS_FILE
        stats = StatsCommand().load_stats() if os.path.exists(stats_file) else {}
        stats['commands_executed'] = stats.get('commands_executed', 0) + 1
        StatsCommand()._save_stats(stats)
