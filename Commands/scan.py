"""Advanced Scan command with real-time analysis and PyQt5 GUI"""

import os
import hashlib
import subprocess
import sys
from Commands import Command

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                                  QListWidget, QListWidgetItem, QTextEdit, QPushButton, 
                                  QTabWidget, QLabel, QProgressBar, QMessageBox)
    from PyQt5.QtCore import Qt
    from PyQt5.QtGui import QFont, QColor, QTextCursor, QTextCharFormat
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False


class ScanCommand(Command):
    """Advanced scan with real-time threat analysis"""
    name = "scan"
    description = "Advanced scan with real-time threat detection"
    usage = "scan [path]"
    
    DANGEROUS_SIGNATURES = {
        b'MZ': 'PE Executable (EXE/DLL)',
        b'PK\x03\x04': 'ZIP/Office Document',
        b'Rar!': 'RAR Archive',
        b'\x1f\x8b\x08': 'GZIP Compressed',
    }
    
    SUSPICIOUS_EXTENSIONS = ['.exe', '.bat', '.cmd', '.vbs', '.ps1', '.scr', '.msi', 
                             '.dll', '.sys', '.drv', '.jar', '.zip', '.rar']
    
    SUSPICIOUS_KEYWORDS = [
        b'GetProcAddress', b'CreateRemoteThread', b'WriteProcessMemory', 
        b'VirtualAlloc', b'ShellExecute', b'WinExec', b'cmd.exe', b'powershell',
        b'regsvcs', b'InstallUtil', b'rundll32'
    ]
    
    def __init__(self):
        super().__init__()
        self.suspicious_files = []
    
    def execute(self, args):
        """Execute scan"""
        path = args[0] if args else "."
        
        if not os.path.exists(path):
            print(f"Path not found: {path}")
            return
        
        print(f"\n🔍 Scanning: {path}")
        print("Analyzing files...\n")
        
        self.suspicious_files = []
        scanned = 0
        
        try:
            for root, dirs, files in os.walk(path):
                for file in files:
                    filepath = os.path.join(root, file)
                    scanned += 1
                    threat_info = self._analyze_file(filepath)
                    if threat_info:
                        self.suspicious_files.append((filepath, threat_info))
            
            # Sort by risk
            self.suspicious_files.sort(key=lambda x: x[1]['risk'], reverse=True)
            
            print(f"✓ Scanned {scanned} files")
            print(f"⚠️  Found {len(self.suspicious_files)} threats\n")
            
            if self.suspicious_files and PYQT5_AVAILABLE:
                self._show_gui()
            elif self.suspicious_files:
                self._show_text()
            else:
                print("✓ No threats detected")
        except Exception as e:
            print(f"Error: {e}")
    
    def _analyze_file(self, filepath):
        """Analyze file for threats"""
        try:
            with open(filepath, 'rb') as f:
                data = f.read(50000)
        except:
            return None
        
        if not data:
            return None
        
        ext = os.path.splitext(filepath)[1].lower()
        size = os.path.getsize(filepath)
        threats = []
        risk = 0
        keywords = {}
        
        # Check signature
        for sig, desc in self.DANGEROUS_SIGNATURES.items():
            if data.startswith(sig):
                if ext in self.SUSPICIOUS_EXTENSIONS:
                    threats.append(('CRITICAL', f"Dangerous signature: {desc}"))
                    risk += 40
                break
        
        # Check keywords
        for keyword in self.SUSPICIOUS_KEYWORDS:
            count = data.count(keyword)
            if count > 0:
                keywords[keyword.decode('utf-8', errors='ignore')] = count
        
        if len(keywords) >= 3:
            threats.append(('CRITICAL', f"{len(keywords)} suspicious APIs"))
            risk += 35
        elif len(keywords) >= 2:
            threats.append(('HIGH', f"{len(keywords)} suspicious APIs"))
            risk += 20
        elif len(keywords):
            threats.append(('MEDIUM', "Suspicious keyword found"))
            risk += 10
        
        # Check extension
        if ext in self.SUSPICIOUS_EXTENSIONS:
            if data.startswith(b'MZ'):
                threats.append(('CRITICAL', f"Executable: {ext}"))
                risk += 30
            elif ext in ['.bat', '.cmd', '.ps1', '.vbs']:
                threats.append(('HIGH', f"Script: {ext}"))
                risk += 25
        
        # Check size
        if data.startswith(b'MZ') and size > 10*1024*1024:
            threats.append(('HIGH', "Large executable (possible packer)"))
            risk += 15
        
        # Entropy
        entropy = self._entropy(data[:5000])
        if entropy > 7.5:
            threats.append(('MEDIUM', f"High entropy (obfuscated)"))
            risk += 15
        
        if threats:
            return {
                'threats': threats,
                'risk': min(risk, 100),
                'size': size,
                'keywords': keywords,
                'entropy': entropy
            }
        return None
    
    def _entropy(self, data):
        """Calculate entropy"""
        if not data:
            return 0
        entropy = 0
        for i in range(256):
            p = data.count(bytes([i])) / len(data)
            if p > 0:
                entropy += -p * (p ** 2)
        return min(entropy, 8)
    
    def _show_text(self):
        """Show text results"""
        for filepath, info in self.suspicious_files[:10]:
            risk = info['risk']
            symbol = "🔴" if risk >= 80 else "🟠" if risk >= 60 else "🟡"
            print(f"{symbol} {risk}% - {filepath}")
            for level, threat in info['threats']:
                print(f"  ⚠️  {threat}")
    
    def _show_gui(self):
        """Show PyQt5 GUI"""
        app = QApplication.instance() or QApplication(sys.argv)
        window = ScanWindow(self.suspicious_files)
        window.show()
        app.exec_()


class ScanWindow(QMainWindow):
    """PyQt5 scan results window"""
    
    def __init__(self, files):
        super().__init__()
        self.files = files
        self.current = None
        self.init_ui()
    
    def init_ui(self):
        """Initialize UI"""
        self.setWindowTitle("🔍 EchoShell Scanner")
        self.setGeometry(50, 50, 1400, 800)
        self.setStyleSheet(self._stylesheet())
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QHBoxLayout()
        
        # LEFT: File list
        left = QVBoxLayout()
        title = QLabel("🔴 THREATS DETECTED")
        title.setFont(QFont("Arial", 13, QFont.Bold))
        left.addWidget(title)
        
        self.list = QListWidget()
        self.list.itemClicked.connect(self.on_select)
        self.list.setMinimumWidth(350)
        
        for filepath, info in self.files:
            risk = info['risk']
            name = os.path.basename(filepath)
            threats = len(info['threats'])
            
            # Risk label
            if risk >= 80:
                icon = "🔴 CRITICAL"
            elif risk >= 60:
                icon = "🟠 HIGH"
            elif risk >= 40:
                icon = "🟡 MEDIUM"
            else:
                icon = "🟢 LOW"
            
            item = QListWidgetItem(f"{name}\n{icon} ({risk}%) • {threats} threats")
            item.setData(Qt.UserRole, (filepath, info))
            
            # Color
            if risk >= 80:
                item.setBackground(QColor(255, 100, 100, 100))
            elif risk >= 60:
                item.setBackground(QColor(255, 165, 0, 100))
            elif risk >= 40:
                item.setBackground(QColor(255, 255, 0, 100))
            
            self.list.addItem(item)
        
        left.addWidget(self.list)
        
        # RIGHT: Details
        right = QVBoxLayout()
        
        title = QLabel("📋 ANALYSIS")
        title.setFont(QFont("Arial", 13, QFont.Bold))
        right.addWidget(title)
        
        # Risk bar
        self.risk_label = QLabel("Risk: 0%")
        self.risk_label.setFont(QFont("Arial", 11, QFont.Bold))
        right.addWidget(self.risk_label)
        
        self.risk_bar = QProgressBar()
        self.risk_bar.setMaximum(100)
        self.risk_bar.setMaximumHeight(20)
        right.addWidget(self.risk_bar)
        
        # Tabs
        self.tabs = QTabWidget()
        
        self.summary = QTextEdit()
        self.summary.setReadOnly(True)
        self.summary.setFont(QFont("Courier", 10))
        self.tabs.addTab(self.summary, "📊 Summary")
        
        self.threats = QTextEdit()
        self.threats.setReadOnly(True)
        self.threats.setFont(QFont("Courier", 10))
        self.tabs.addTab(self.threats, "⚠️  Threats")
        
        self.text = QTextEdit()
        self.text.setReadOnly(True)
        self.text.setFont(QFont("Courier", 9))
        self.tabs.addTab(self.text, "📝 Text")
        
        self.hexview = QTextEdit()
        self.hexview.setReadOnly(True)
        self.hexview.setFont(QFont("Courier", 8))
        self.tabs.addTab(self.hexview, "🔢 Hex")
        
        right.addWidget(self.tabs)
        
        # Buttons
        btns = QHBoxLayout()
        
        self.open = QPushButton("📂 Open")
        self.open.clicked.connect(self.open_file)
        self.open.setStyleSheet("background: #ff6b6b; color: white; font-weight: bold;")
        btns.addWidget(self.open)
        
        self.delete = QPushButton("🗑️  Delete")
        self.delete.clicked.connect(self.delete_file)
        self.delete.setStyleSheet("background: #ff9800; color: white; font-weight: bold;")
        btns.addWidget(self.delete)
        
        close = QPushButton("Close")
        close.clicked.connect(self.close)
        btns.addWidget(close)
        
        right.addLayout(btns)
        
        layout.addLayout(left, 1)
        layout.addLayout(right, 2)
        central.setLayout(layout)
        
        if self.files:
            self.list.setCurrentRow(0)
            self.on_select(self.list.item(0))
    
    def on_select(self, item):
        """File selected"""
        filepath, info = item.data(Qt.UserRole)
        self.current = filepath
        self.current_info = info
        
        risk = info['risk']
        self.risk_bar.setValue(risk)
        self.risk_label.setText(f"Risk: {risk}%")
        
        if risk >= 80:
            self.risk_bar.setStyleSheet("QProgressBar::chunk { background: #ff4444; }")
        elif risk >= 60:
            self.risk_bar.setStyleSheet("QProgressBar::chunk { background: #ff9800; }")
        else:
            self.risk_bar.setStyleSheet("QProgressBar::chunk { background: #ffeb3b; }")
        
        # Summary
        size = info['size']
        self.summary.setText(f"""
📄 File Info
{'='*70}

Path: {filepath}
Size: {size:,} bytes ({size/1024/1024:.2f} MB)
Threats: {len(info['threats'])}
Risk: {risk}/100
Entropy: {info['entropy']:.2f}/8.0
""")
        
        # Threats with colors
        self.threats.clear()
        cursor = self.threats.textCursor()
        
        fmt = QTextCharFormat()
        fmt.setFont(QFont("Arial", 11, QFont.Bold))
        cursor.insertText("Detected Threats\n", fmt)
        cursor.insertText("="*70 + "\n\n")
        
        for level, threat in info['threats']:
            fmt = QTextCharFormat()
            fmt.setFont(QFont("Courier", 10, QFont.Bold))
            
            if level == 'CRITICAL':
                fmt.setForeground(QColor(255, 50, 50))
                symbol = "🔴 CRITICAL: "
            elif level == 'HIGH':
                fmt.setForeground(QColor(255, 150, 0))
                symbol = "🟠 HIGH: "
            else:
                fmt.setForeground(QColor(255, 200, 0))
                symbol = "🟡 MEDIUM: "
            
            cursor.insertText(symbol, fmt)
            cursor.insertText(threat + "\n")
        
        # Keywords
        if info['keywords']:
            cursor.insertText("\n" + "="*70 + "\n")
            fmt = QTextCharFormat()
            fmt.setFont(QFont("Arial", 10, QFont.Bold))
            fmt.setForeground(QColor(200, 0, 0))
            cursor.insertText("Suspicious APIs\n", fmt)
            cursor.insertText("="*70 + "\n")
            for kw, count in sorted(info['keywords'].items(), key=lambda x: x[1], reverse=True):
                cursor.insertText(f"  • {kw}: {count} times\n")
        
        self.threats.setTextCursor(cursor)
        
        # Preview
        try:
            with open(filepath, 'rb') as f:
                data = f.read(3000)
            self.text.setText(data.decode('utf-8', errors='replace'))
        except:
            self.text.setText("Error reading file")
        
        # Hex
        try:
            with open(filepath, 'rb') as f:
                data = f.read(1500)
            
            hex_text = ""
            for i in range(0, len(data), 16):
                chunk = data[i:i+16]
                hex_str = ' '.join(f'{b:02x}' for b in chunk)
                ascii_str = ''.join(chr(b) if 32 <= b < 127 else '.' for b in chunk)
                hex_text += f"{i:08x}  {hex_str:<48}  {ascii_str}\n"
            
            self.hexview.setText(hex_text)
        except:
            self.hexview.setText("Error reading file")
    
    def open_file(self):
        """Open file"""
        if not self.current:
            return
        
        reply = QMessageBox.critical(
            self, "⚠️  WARNING",
            f"File is DANGEROUS!\n\n{self.current}",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                if os.name == 'nt':
                    os.startfile(self.current)
                else:
                    subprocess.Popen(['xdg-open', self.current])
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
    
    def delete_file(self):
        """Delete file"""
        if not self.current:
            return
        
        reply = QMessageBox.warning(
            self, "🗑️  Delete",
            f"Delete permanently?\n\n{self.current}",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            try:
                os.remove(self.current)
                QMessageBox.information(self, "Success", "File deleted!")
                
                idx = self.list.currentRow()
                self.list.takeItem(idx)
                
                if self.list.count() > 0:
                    self.list.setCurrentRow(0)
                    self.on_select(self.list.item(0))
                else:
                    self.summary.setText("✓ All threats removed!")
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
    
    def _stylesheet(self):
        """Get CSS"""
        return """
        QMainWindow { background-color: #f5f5f5; }
        QLabel { color: #333; }
        QTextEdit { background-color: #fff; color: #333; border: 1px solid #ddd; border-radius: 4px; }
        QListWidget { background-color: #fff; border: 1px solid #ddd; border-radius: 4px; }
        QListWidget::item { padding: 10px; border-bottom: 1px solid #eee; }
        QListWidget::item:selected { background-color: #e3f2fd; }
        QPushButton { background-color: #2196F3; color: white; border: none; border-radius: 4px; padding: 8px 16px; font-weight: bold; }
        QPushButton:hover { background-color: #1976D2; }
        QTabWidget::pane { border: 1px solid #ddd; }
        QTabBar::tab { background-color: #f0f0f0; color: #333; padding: 8px 20px; border: 1px solid #ddd; }
        QTabBar::tab:selected { background-color: #2196F3; color: white; }
        """


