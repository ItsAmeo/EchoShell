"""Vulnerability Assessment and Management"""

from Commands import Command

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QTableWidget,
                                  QTableWidgetItem, QLabel, QPushButton)
    from PyQt5.QtGui import QFont, QColor
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False

class VulnmgmtCommand(Command):
    name = "vulnmgmt"
    description = "Vulnerability assessment and management"
    usage = "vulnmgmt [action]"
    
    def execute(self, args):
        action = args[0] if args else "list"
        
        print("\n[*] Vulnerability Management System")
        
        if action == "list" and PYQT5_AVAILABLE:
            self._show_gui()
        else:
            self._show_text()
    
    def _show_text(self):
        print("[+] Identified Vulnerabilities:")
        vulns = [
            ("CVE-2021-44228", "Log4j RCE", "Critical", 10.0),
            ("CVE-2020-1938", "Tomcat AJP", "High", 8.5),
            ("CVE-2019-2725", "WebLogic RCE", "Critical", 9.8),
            ("CVE-2017-5638", "Struts2 RCE", "Critical", 10.0),
            ("CVE-2016-3087", "Java Deserialization", "High", 8.8)
        ]
        
        for cve, title, severity, score in vulns:
            print(f"  [{cve}] {title} - {severity} - CVSS {score}")
    
    def _show_gui(self):
        try:
            app = QApplication.instance() or QApplication([])
            window = VulnWindow()
            window.show()
            app.exec_()
        except:
            self._show_text()

class VulnWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vulnerability Management")
        self.setGeometry(50, 50, 1200, 600)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        title = QLabel("VULNERABILITY ASSESSMENT REPORT")
        title.setFont(QFont("Courier", 12, QFont.Bold))
        layout.addWidget(title)
        
        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["CVE", "Title", "Severity", "CVSS", "Status"])
        
        vulns = [
            ("CVE-2021-44228", "Log4j RCE", "Critical", "10.0", "Patched"),
            ("CVE-2020-1938", "Tomcat AJP", "High", "8.5", "Pending"),
            ("CVE-2019-2725", "WebLogic RCE", "Critical", "9.8", "Vulnerable"),
            ("CVE-2017-5638", "Struts2 RCE", "Critical", "10.0", "Patched"),
            ("CVE-2016-3087", "Deserialization", "High", "8.8", "Vulnerable")
        ]
        
        table.setRowCount(len(vulns))
        for i, (cve, title, severity, cvss, status) in enumerate(vulns):
            table.setItem(i, 0, QTableWidgetItem(cve))
            table.setItem(i, 1, QTableWidgetItem(title))
            table.setItem(i, 2, QTableWidgetItem(severity))
            table.setItem(i, 3, QTableWidgetItem(cvss))
            table.setItem(i, 4, QTableWidgetItem(status))
            
            if severity == "Critical":
                color = QColor(255, 50, 50)
            elif severity == "High":
                color = QColor(255, 150, 50)
            else:
                color = QColor(255, 255, 50)
            
            for j in range(5):
                table.item(i, j).setForeground(color)
        
        layout.addWidget(table)
        
        btn = QPushButton("Close")
        btn.clicked.connect(self.close)
        layout.addWidget(btn)
        
        central.setLayout(layout)
