#!/usr/bin/env python3
"""
EchoShell Auto-Update - Standalone updater at project root
Safely updates all files from GitHub, including main.py
"""

import os
import urllib.request
import json
import sys
import hashlib

class EchoShellUpdater:
    """Standalone updater for EchoShell"""
    GITHUB_REPO = "ItsAmeo/EchoShell"
    GITHUB_API = "https://api.github.com/repos/ItsAmeo/EchoShell/git/trees/main?recursive=1"
    GITHUB_RAW = "https://raw.githubusercontent.com/ItsAmeo/EchoShell/main"
    
    def __init__(self):
        # Workspace root is the directory this script is in
        self.workspace_root = os.path.dirname(os.path.abspath(__file__))
        print(f"\n{'='*70}")
        print(f"🔄 EchoShell Auto-Update")
        print(f"{'='*70}")
        print(f"📁 Workspace: {self.workspace_root}\n")
    
    def run(self):
        """Execute the update"""
        try:
            print("📥 Fetching file list from GitHub...\n")
            
            # Get remote files
            remote_files = self._get_all_remote_files()
            
            if not remote_files:
                print("❌ Could not fetch files from GitHub")
                return False
            
            print(f"✓ Found {len(remote_files)} files on GitHub\n")
            
            # STEP 1: Delete files that exist locally but NOT on GitHub
            print("🔍 Checking for deleted files on GitHub...\n")
            local_files = self._get_local_files()
            
            files_to_delete = []
            for local_file in local_files:
                if local_file not in remote_files:
                    # Don't delete config or output folders
                    if not any(x in local_file for x in ['Config/', '1-Output/', '.git']):
                        files_to_delete.append(local_file)
            
            deleted_count = 0
            if files_to_delete:
                print(f"🗑️  Found {len(files_to_delete)} files to delete (removed from GitHub):\n")
                for filepath in files_to_delete:
                    local_path = os.path.join(self.workspace_root, filepath)
                    try:
                        if os.path.exists(local_path):
                            os.remove(local_path)
                            print(f"  🗑️  {filepath}")
                            deleted_count += 1
                    except Exception as e:
                        print(f"  ⚠️  Could not delete {filepath}: {e}")
                print(f"\n✓ Deleted {deleted_count} obsolete files\n")
            else:
                print("✓ No files to delete\n")
            
            # STEP 2: DELETE main.py FIRST to force update
            main_py_path = os.path.join(self.workspace_root, 'main.py')
            if os.path.exists(main_py_path):
                print(f"🗑️  Deleting old main.py...")
                try:
                    os.remove(main_py_path)
                    print(f"✓ main.py deleted\n")
                except Exception as e:
                    print(f"⚠️  Could not delete main.py: {e}")
                    print(f"   Will overwrite instead\n")
            
            # STEP 3: Download/update all files from GitHub
            to_download = []
            skipped = 0
            
            for filepath in sorted(remote_files):
                # Skip ONLY .git and __pycache__ folders
                if '.git' in filepath or '__pycache__' in filepath or '.DS_Store' in filepath:
                    skipped += 1
                    continue
                
                local_path = os.path.join(self.workspace_root, filepath)
                to_download.append((filepath, local_path))
            
            print(f"📋 Files to download/update: {len(to_download)}\n")
            print("Downloading files:\n")
            
            if not to_download:
                print("✓ All files up to date!\n")
                return True
            
            # Download all files
            success = 0
            failed = 0
            updated_files = []
            
            for filepath, local_path in to_download:
                try:
                    url = f"{self.GITHUB_RAW}/{filepath}"
                    
                    # Check if file exists and compare
                    was_updated = self._download_file(filepath, url, local_path)
                    
                    if was_updated:
                        updated_files.append(filepath)
                        if filepath == 'main.py':
                            print(f"  ✓ {filepath} ⭐ [FRESH FROM GITHUB - CRITICAL]")
                        else:
                            print(f"  ✓ {filepath}")
                        success += 1
                    else:
                        # File was written successfully
                        success += 1
                        if filepath == 'main.py':
                            print(f"  ✓ {filepath} [REINSTALLED]")
                        else:
                            print(f"  ✓ {filepath}")
                
                except Exception as e:
                    print(f"  ❌ {filepath}: {str(e)}")
                    failed += 1
            
            # Verify main.py was actually written
            main_py_path = os.path.join(self.workspace_root, 'main.py')
            if os.path.exists(main_py_path):
                size = os.path.getsize(main_py_path)
                print(f"\n✓ Verification: main.py exists ({size} bytes)")
            else:
                print(f"\n❌ ERROR: main.py NOT FOUND after update!")
            
            print(f"\n{'='*70}")
            print(f"✓ UPDATE COMPLETE - FULL SYNC WITH GITHUB")
            print(f"{'='*70}")
            print(f"✓ {success} files downloaded/updated")
            if failed > 0:
                print(f"❌ {failed} failed")
            if skipped > 0:
                print(f"⊘ {skipped} files skipped")
            if deleted_count > 0:
                print(f"🗑️  {deleted_count} obsolete files deleted")
            print(f"{'='*70}\n")
            
            return True
            
        except Exception as e:
            print(f"\n❌ Error during update: {e}\n")
            import traceback
            traceback.print_exc()
            return False
    
    def _get_all_remote_files(self):
        """Get all files from GitHub using git tree API"""
        try:
            req = urllib.request.Request(self.GITHUB_API)
            req.add_header('User-Agent', 'Mozilla/5.0')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                data = json.loads(response.read().decode())
            
            files = []
            if 'tree' in data:
                for item in data['tree']:
                    if item['type'] == 'blob':  # blob = file
                        files.append(item['path'])
            
            return files
        
        except Exception as e:
            print(f"Error fetching GitHub tree: {e}")
            import traceback
            traceback.print_exc()
            return []
    
    def _get_local_files(self):
        """Get all local files relative to workspace root"""
        files = []
        for root, dirs, filenames in os.walk(self.workspace_root):
            # Skip certain directories
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', '.venv', 'venv']]
            
            for filename in filenames:
                filepath = os.path.join(root, filename)
                # Get relative path
                rel_path = os.path.relpath(filepath, self.workspace_root)
                # Normalize to forward slashes for consistency
                rel_path = rel_path.replace('\\', '/')
                files.append(rel_path)
        
        return files
    
    def _download_file(self, filepath, url, local_path):
        """Download file from GitHub and save it. Returns True if updated, False if already exists with same content"""
        try:
            # Create directory if needed
            dir_path = os.path.dirname(local_path)
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path, exist_ok=True)
            
            # Download file
            req = urllib.request.Request(url)
            req.add_header('User-Agent', 'Mozilla/5.0')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                content = response.read()
            
            # Check if file already exists with same content
            was_updated = True
            if os.path.exists(local_path):
                try:
                    with open(local_path, 'rb') as f:
                        existing_content = f.read()
                    if existing_content == content:
                        was_updated = False
                except:
                    pass
            
            # Write file (always, to ensure it's saved)
            with open(local_path, 'wb') as f:
                f.write(content)
            
            # Verify it was written
            if not os.path.exists(local_path):
                raise Exception(f"File was not saved to {local_path}")
            
            return was_updated
        
        except Exception as e:
            raise Exception(f"Download failed: {e}")


def main():
    """Main entry point"""
    updater = EchoShellUpdater()
    success = updater.run()
    
    if success:
        print("✨ Update successful! You can now run EchoShell again.\n")
        input("Press Enter to exit...")
        sys.exit(0)
    else:
        print("⚠️ Update had issues. Check the output above.\n")
        input("Press Enter to exit...")
        sys.exit(1)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")
        sys.exit(1)

