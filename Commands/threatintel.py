"""Advanced Threat Intelligence Platform"""

from Commands import Command

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                                  QTableWidget, QTableWidgetItem, QLabel, QPushButton, QTextEdit)
    from PyQt5.QtGui import QFont, QColor
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False

class ThreatintelCommand(Command):
    name = "threatintel"
    description = "Advanced threat intelligence dashboard"
    usage = "threatintel [action]"
    
    def execute(self, args):
        action = args[0] if args else "dashboard"
        
        print("\n[*] Threat Intelligence Platform")
        
        if action == "dashboard" and PYQT5_AVAILABLE:
            self._show_dashboard()
        else:
            self._show_text()
    
    def _show_text(self):
        print("[+] Recent Threats:")
        threats = [
            ("Ransomware.Conti", "Critical", "2024-01-08"),
            ("Trojan.AgentTesla", "High", "2024-01-07"),
            ("Botnet.Mirai", "High", "2024-01-06"),
            ("Cryptominer.Generic", "Medium", "2024-01-05"),
            ("Spyware.KeyLogger", "High", "2024-01-04")
        ]
        
        for name, severity, date in threats:
            print(f"  [+] {name} - {severity} - {date}")
    
    def _show_dashboard(self):
        try:
            app = QApplication.instance() or QApplication([])
            window = ThreatDashboard()
            window.show()
            app.exec_()
        except:
            self._show_text()

class ThreatDashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Threat Intelligence Dashboard")
        self.setGeometry(50, 50, 1000, 600)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        title = QLabel("THREAT INTELLIGENCE PLATFORM")
        title.setFont(QFont("Courier", 14, QFont.Bold))
        layout.addWidget(title)
        
        # Threats table
        table = QTableWidget()
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(["Threat Name", "Severity", "Date", "Status"])
        
        threats = [
            ("Ransomware.Conti", "Critical", "2024-01-08", "Active"),
            ("Trojan.AgentTesla", "High", "2024-01-07", "Monitored"),
            ("Botnet.Mirai", "High", "2024-01-06", "Active"),
            ("Cryptominer.Generic", "Medium", "2024-01-05", "Contained"),
            ("Spyware.KeyLogger", "High", "2024-01-04", "Detected")
        ]
        
        table.setRowCount(len(threats))
        for i, (name, severity, date, status) in enumerate(threats):
            table.setItem(i, 0, QTableWidgetItem(name))
            table.setItem(i, 1, QTableWidgetItem(severity))
            table.setItem(i, 2, QTableWidgetItem(date))
            table.setItem(i, 3, QTableWidgetItem(status))
            
            if severity == "Critical":
                color = QColor(255, 50, 50)
            elif severity == "High":
                color = QColor(255, 150, 50)
            else:
                color = QColor(255, 255, 50)
            
            for j in range(4):
                table.item(i, j).setForeground(color)
        
        layout.addWidget(table)
        
        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.close)
        layout.addWidget(close_btn)
        
        central.setLayout(layout)
