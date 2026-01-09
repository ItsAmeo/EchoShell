"""Network Traffic Analysis"""

from Commands import Command

try:
    from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                                  QTableWidget, QTableWidgetItem, QLabel, QPushButton)
    from PyQt5.QtGui import QFont, QColor
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False

class PacketCommand(Command):
    name = "packet"
    description = "Packet capture and analysis"
    usage = "packet [action]"
    
    def execute(self, args):
        action = args[0] if args else "analyze"
        
        print(f"\n[*] Network Packet Analysis")
        
        if action == "analyze" and PYQT5_AVAILABLE:
            self._show_gui()
        else:
            self._show_text()
    
    def _show_text(self):
        print("[+] Captured Packets:")
        packets = [
            ("TCP", "192.168.1.1", "192.168.1.100", "80", "SYN"),
            ("TCP", "192.168.1.100", "93.184.216.34", "443", "HTTPS"),
            ("UDP", "192.168.1.100", "8.8.8.8", "53", "DNS"),
            ("TCP", "192.168.1.50", "192.168.1.100", "22", "SSH"),
            ("ICMP", "192.168.1.1", "192.168.1.100", "0", "PING")
        ]
        
        for proto, src, dst, port, flag in packets:
            print(f"  [+] {proto} {src} -> {dst}:{port} ({flag})")
    
    def _show_gui(self):
        try:
            app = QApplication.instance() or QApplication([])
            window = PacketWindow()
            window.show()
            app.exec_()
        except:
            self._show_text()

class PacketWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Packet Analyzer")
        self.setGeometry(50, 50, 1200, 600)
        
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout()
        
        title = QLabel("NETWORK PACKET CAPTURE")
        title.setFont(QFont("Courier", 12, QFont.Bold))
        layout.addWidget(title)
        
        table = QTableWidget()
        table.setColumnCount(5)
        table.setHorizontalHeaderLabels(["Protocol", "Source", "Destination", "Port", "Flag"])
        
        packets = [
            ("TCP", "192.168.1.1", "192.168.1.100", "80", "SYN"),
            ("TCP", "192.168.1.100", "93.184.216.34", "443", "HTTPS"),
            ("UDP", "192.168.1.100", "8.8.8.8", "53", "DNS"),
            ("TCP", "192.168.1.50", "192.168.1.100", "22", "SSH"),
            ("ICMP", "192.168.1.1", "192.168.1.100", "0", "PING")
        ]
        
        table.setRowCount(len(packets))
        for i, (proto, src, dst, port, flag) in enumerate(packets):
            table.setItem(i, 0, QTableWidgetItem(proto))
            table.setItem(i, 1, QTableWidgetItem(src))
            table.setItem(i, 2, QTableWidgetItem(dst))
            table.setItem(i, 3, QTableWidgetItem(port))
            table.setItem(i, 4, QTableWidgetItem(flag))
        
        layout.addWidget(table)
        
        btn = QPushButton("Close")
        btn.clicked.connect(self.close)
        layout.addWidget(btn)
        
        central.setLayout(layout)
