"""Intrusion Detection System (IDS)"""

from Commands import Command

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                                  QListWidget, QListWidgetItem, QLabel, QPushButton)
    from PyQt5.QtGui import QFont, QColor
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False

class IdsCommand(Command):
    name = "ids"
    description = "Intrusion detection system monitoring"
    usage = "ids [action]"
    
    def execute(self, args):
        action = args[0] if args else "alerts"
        
        print(f"\n[*] Intrusion Detection System")
        
        if action == "alerts" and PYQT5_AVAILABLE:
            self._show_gui()
        else:
            self._show_text()
    
    def _show_text(self):
        print("[+] Active Alerts:")
        alerts = [
            ("SQL Injection Attempt", "Critical", "192.168.1.50", "80"),
            ("Brute Force Attack", "High", "192.168.1.51", "22"),
            ("Port Scan", "Medium", "192.168.1.100", "1-65535"),
            ("DDoS Attack", "Critical", "0.0.0.0", "80"),
            ("Shellcode Detected", "Critical", "192.168.1.75", "443")
        ]
        
        for alert, severity, src, dst in alerts:
            print(f"  [{severity}] {alert} - From {src} to {dst}")
    
    def _show_gui(self):
        try:
            app = QApplication.instance() or QApplication([])
            window = IDSWindow()
            window.show()
            app.exec_()
        except:
            self._show_text()

class IDSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Intrusion Detection System")
        self.setGeometry(50, 50, 1000, 600)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        title = QLabel("IDS ALERT DASHBOARD")
        title.setFont(QFont("Courier", 12, QFont.Bold))
        layout.addWidget(title)
        
        alerts_list = QListWidget()
        alerts = [
            ("SQL Injection Attempt", "Critical", "192.168.1.50"),
            ("Brute Force Attack", "High", "192.168.1.51"),
            ("Port Scan", "Medium", "192.168.1.100"),
            ("DDoS Attack", "Critical", "0.0.0.0"),
            ("Shellcode Detected", "Critical", "192.168.1.75")
        ]
        
        for alert, severity, src in alerts:
            item_text = f"[{severity}] {alert} - {src}"
            item = QListWidgetItem(item_text)
            
            if severity == "Critical":
                color = QColor(255, 50, 50)
            elif severity == "High":
                color = QColor(255, 150, 50)
            else:
                color = QColor(255, 255, 50)
            
            item.setForeground(color)
            item.setFont(QFont("Courier", 9))
            alerts_list.addItem(item)
        
        layout.addWidget(alerts_list)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        
        central.setLayout(layout)
