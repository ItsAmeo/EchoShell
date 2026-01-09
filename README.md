# EchoShell 🔥

[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=flat-square)](https://github.com/ItsAmeo/EchoShell/releases)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow?style=flat-square&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)](https://github.com/ItsAmeo/EchoShell)
[![Build](https://img.shields.io/badge/Build-PyInstaller-orange?style=flat-square)](https://pyinstaller.org/)

> 🚀 Professional CLI application with authentication, 23+ system commands, malware scanner with PyQt5 GUI, and automatic GitHub sync.

---

## ✨ Features

### 🔐 Security & Authentication
- **Token-Based Access Control** - Protect your CLI with custom tokens
- **Auto-Authentication** - Save tokens for faster login
- **Settings Management** - Control auth behavior with `autoauth` command
- **Discord Webhook Integration** - Get notified when EchoShell opens

### 🖥️ System Commands (23+)
```
sysinfo    ls        pwd       mkdir     rm        copy      tree
ping       curl      dns       calc      clear     echo      search
hash       date      whoami    ip        cd        logs      stats
scan       settings  update    autoauth
```

### 🎨 Advanced Features
- **Gradient Banner** - Beautiful RGB gradient (Red → Orange → Yellow)
- **Interactive REPL** - Real-time command input with auto-completion
- **Command Auto-Discovery** - New commands automatically detected
- **Lazy Loading** - Fast startup times with on-demand command loading
- **Performance Optimized** - <100ms response time per command

### 🔍 Threat Scanner
- **Advanced Malware Detection** - Signature-based file analysis
- **Risk Scoring** - 0-100% threat assessment
- **PyQt5 GUI** - Professional results display with:
  - 🔴 CRITICAL threats in red
  - 🟠 HIGH threats in orange
  - 🟡 MEDIUM threats in yellow
  - 4 analysis tabs: Summary, Threats, Preview, Hex Dump
- **Entropy Detection** - Identifies obfuscated code
- **Keyword Analysis** - Detects suspicious API calls

### 🔄 Auto-Update System
- **GitHub Sync** - Keeps your installation up-to-date
- **Selective Deletion** - Removes files no longer in repo
- **Force Main.py Update** - Always gets latest core
- **Standalone Updater** - `update.exe` works independently
- **Zero-Configuration** - Just run and it works

### 📦 Standalone Executables
- **EchoShell.exe** - Main application (~50MB)
- **EchoShell-Update.exe** - Auto-updater (~40MB)
- **No Python Required** - Runs on any Windows machine

---

## 🚀 Quick Start

### Option 1: From Executables (Easiest)
```powershell
# Download the latest release
# Run EchoShell.exe directly - no Python needed!
.\EchoShell.exe
```

### Option 2: From Source
```powershell
# Clone the repository
git clone https://github.com/ItsAmeo/EchoShell.git
cd EchoShell

# Install dependencies
pip install -r requirements.txt

# Run
python main.py
```

### Option 3: Build Your Own Executables
```powershell
# Build exe files
python build.py

# Then run
.\dist\EchoShell.exe
```

---

## 📖 Usage

### First Login
```
======================================================================
🔐 EchoShell Authentication Required
======================================================================

🔑 Enter access token (3 attempts left): [YOUR_TOKEN_HERE]
```

**Available Tokens:**
- `tQqrK4.;):1,Pk6[o6TqYk#FrZj2:'wVcU7S|m0LW*[I(xCSXS4dQXme0IMY@.k`
- `nX9pL2@mQ$vT#rE&yF*jG(kH)lW,zA.bC[dE]fG{hI|jK:lM;nO'pQ-qR=sT+uV/wX`

### Command Examples
```bash
EchoShell> help                          # Show all commands
EchoShell> sysinfo                       # Display system information
EchoShell> ls C:\Users                   # List directory contents
EchoShell> scan C:\                      # Scan for threats
EchoShell> autoauth status               # Check auto-login status
EchoShell> autoauth disable              # Disable auto-login
EchoShell> update                        # Sync with GitHub
EchoShell> exit                          # Close EchoShell
```

---

## 🔧 Configuration

### Settings.json
Located in `Config/Settings.json`:

```json
{
  "autoauth": "YOUR_TOKEN_HERE",
  "autoauth_enabled": true,
  "theme": "default",
  "notifications_enabled": true
}
```

### Managing Auto-Auth
```bash
EchoShell> autoauth enable      # Turn on auto-login
EchoShell> autoauth disable     # Turn off auto-login
EchoShell> autoauth status      # Check status
```

---

## 📦 Available Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `sysinfo` | System information | `sysinfo` |
| `whoami` | Current user | `whoami` |
| `ls` | List files | `ls [path]` |
| `cd` | Change directory | `cd [path]` |
| `pwd` | Print working directory | `pwd` |
| `mkdir` | Create directory | `mkdir [name]` |
| `rm` | Remove file/folder | `rm [path]` |
| `copy` | Copy file | `copy [src] [dst]` |
| `tree` | Show directory tree | `tree [path]` |
| `ping` | Test connection | `ping [host]` |
| `curl` | HTTP request | `curl [url]` |
| `dns` | DNS lookup | `dns [domain]` |
| `calc` | Calculator | `calc [expression]` |
| `clear` | Clear screen | `clear` |
| `echo` | Print text | `echo [text]` |
| `search` | Find files | `search [pattern] [path]` |
| `hash` | File hash | `hash [file]` |
| `date` | Show date/time | `date` |
| `ip` | Network info | `ip` |
| `logs` | View logs | `logs` |
| `stats` | System stats | `stats` |
| `scan` | Malware scanner | `scan [path]` |
| `settings` | Settings manager | `settings [key] [value]` |
| `autoauth` | Auth manager | `autoauth enable\|disable\|status` |
| `update` | GitHub sync | `update` |

---

## 🏗️ Build System

### Prerequisites
- Python 3.8+
- PyInstaller
- All dependencies in `requirements.txt`

### Building

```powershell
# Automatic setup and build
python setup.py

# OR manual build
python build.py

# Test the build
python test_build.py
```

### Output
- `dist/EchoShell.exe` - Main application (~50MB)
- `dist/EchoShell-Update.exe` - Auto-updater (~40MB)

Both executables run in **console mode** and stay open for interaction.

---

## 📁 Project Structure

```
EchoShell/
├── main.py                 # Entry point + CLI interface
├── update.py               # Auto-updater (standalone)
├── ai.py                   # Advanced AI assistant
├── build.py                # Build system
├── setup.py                # Setup script
├── test_build.py          # Build test
├── build.bat              # Build batch script
├── requirements.txt       # Python dependencies
│
├── Commands/              # Command modules
│   ├── __init__.py
│   ├── scan.py           # Malware scanner with PyQt5 GUI
│   ├── autoauth.py       # Auth manager
│   ├── update.py         # Update command
│   └── [23 other commands]
│
├── Config/               # Configuration
│   └── Settings.json    # User settings
│
└── 1-Output/            # Generated files
    ├── logs/
    ├── stats/
    └── scans/
```

---

## 🔌 Dependencies

```
requests>=2.28.0      # HTTP requests
colorama>=0.4.6       # Terminal colors
psutil>=5.9.0         # System info
PyQt5>=5.15.0         # GUI components
```

**Optional for developers:**
- `pyinstaller>=5.0.0` - For building executables

---

## 🎯 Performance

- **Startup Time:** <500ms (with auto-auth)
- **Command Response:** <100ms
- **Memory Usage:** ~30-50MB
- **File Scanner:** 1000 files/second

---

## 🔐 Security Features

✅ Token-based authentication
✅ Auto-auth with secure token storage
✅ Malware signature detection
✅ Entropy analysis for obfuscation
✅ Suspicious API keyword detection
✅ Discord webhook notifications
✅ Automatic file validation on updates

---

## 🐛 Troubleshooting

### Exe won't open
- Make sure Windows Defender allows it
- Try running as Administrator
- Check Windows 10+ (builds 1909+)

### Commands not loading
- Check that Commands folder exists
- Verify `__init__.py` is present
- Check Python version (3.8+)

### Update fails
- Check internet connection
- Verify GitHub repo is accessible
- Check file permissions

### Scanner slow on large folders
- This is normal for first scans
- Results are cached for speed
- Consider scanning specific folders

---

## 🚀 Future Roadmap

- [ ] Web-based dashboard
- [ ] Remote command execution
- [ ] Multi-language support
- [ ] Plugin system
- [ ] Advanced firewall rules
- [ ] Real-time file monitoring
- [ ] Encrypted command history

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 💬 Support

- 📧 Email: [your-email@example.com]
- 🐛 Issues: [GitHub Issues](https://github.com/ItsAmeo/EchoShell/issues)
- 💭 Discussions: [GitHub Discussions](https://github.com/ItsAmeo/EchoShell/discussions)

---

## 🙏 Credits

**Built with:**
- Python 3.8+
- PyInstaller
- PyQt5
- Colorama
- Requests

**Inspired by:**
- Professional CLI tools
- System administration utilities
- Security analysis frameworks

---

## 📊 Stats

![GitHub stars](https://img.shields.io/github/stars/ItsAmeo/EchoShell?style=social)
![GitHub forks](https://img.shields.io/github/forks/ItsAmeo/EchoShell?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/ItsAmeo/EchoShell?style=social)

---

## 🎉 Thank You!

Thanks for checking out EchoShell! If you find it useful, please consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting features
- 🤝 Contributing code

**Happy hacking!** 🔥

---

<div align="center">

Made with ❤️ by [ItsAmeo](https://github.com/ItsAmeo)

[⬆ Back to top](#echoshell-)

</div>
