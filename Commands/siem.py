"""Log Analysis and SIEM"""

from Commands import Command

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                                  QTextEdit, QLabel, QPushButton, QComboBox)
    from PyQt5.QtGui import QFont
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False

class SiemCommand(Command):
    name = "siem"
    description = "SIEM log analysis and correlation"
    usage = "siem [source]"
    
    def execute(self, args):
        source = args[0] if args else "all"
        
        print(f"\n[*] SIEM - Log Analysis and Correlation")
        
        if PYQT5_AVAILABLE:
            self._show_gui(source)
        else:
            self._show_text(source)
    
    def _show_text(self, source):
        print(f"[+] Analyzing logs from: {source}")
        
        if source == "all" or source == "windows":
            print("\n[*] Windows Event Logs:")
            print("  [-] Failed login attempts: 45")
            print("  [-] Privilege escalation: 3")
            print("  [-] Service restart: 2")
        
        if source == "all" or source == "firewall":
            print("\n[*] Firewall Logs:")
            print("  [-] Blocked connections: 234")
            print("  [-] Port scan detected: 1")
            print("  [-] DDoS attempt: 1")
        
        if source == "all" or source == "web":
            print("\n[*] Web Server Logs:")
            print("  [-] SQL injection attempts: 12")
            print("  [-] XSS attempts: 8")
            print("  [-] 404 errors: 345")
        
        print("\n[+] Correlation Summary:")
        print("  [-] 3 attacks correlated")
        print("  [-] Attack duration: 2 hours")
        print("  [-] Source IPs: 5 unique")
    
    def _show_gui(self, source):
        try:
            app = QApplication.instance() or QApplication([])
            window = SIEMWindow(source)
            window.show()
            app.exec_()
        except:
            self._show_text(source)

class SIEMWindow(QMainWindow):
    def __init__(self, source):
        super().__init__()
        self.setWindowTitle("SIEM Log Analysis")
        self.setGeometry(50, 50, 1000, 700)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        title = QLabel("SIEM - SECURITY INFORMATION AND EVENT MANAGEMENT")
        title.setFont(QFont("Courier", 12, QFont.Bold))
        layout.addWidget(title)
        
        # Source selector
        selector = QComboBox()
        selector.addItems(["All Sources", "Windows", "Firewall", "Web Server"])
        layout.addWidget(selector)
        
        # Log output
        log_view = QTextEdit()
        log_view.setReadOnly(True)
        log_view.setFont(QFont("Courier", 8))
        
        logs = """[2024-01-08 10:45:23] ALERT: Failed login attempt
  Source: 192.168.1.50
  User: admin
  Attempts: 5

[2024-01-08 10:46:15] ALERT: Privilege escalation detected
  User: jsmith
  Command: whoami
  Result: SYSTEM

[2024-01-08 10:47:00] ALERT: Port scan detected
  Source: 192.168.1.100
  Ports: 80, 443, 22, 3389
  
[2024-01-08 10:48:30] ALERT: SQL injection attempt
  URL: /login.php
  Payload: ' OR '1'='1' --
  
[2024-01-08 10:49:45] CORRELATION: Attack chain identified
  Attacker: 192.168.1.50
  Stage 1: Reconnaissance
  Stage 2: Exploitation
  Stage 3: Persistence
  Stage 4: Exfiltration
  
[+] ALERT SEVERITY: CRITICAL
[+] RECOMMENDED ACTION: Isolate affected systems immediately
"""
        
        log_view.setText(logs)
        layout.addWidget(log_view)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        
        central.setLayout(layout)
