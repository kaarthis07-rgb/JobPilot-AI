from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JobPilot AI Dashboard")
        self.resize(1000, 700)

        title = QLabel("Welcome to JobPilot AI")
        title.setStyleSheet("font-size:28px; font-weight:bold;")

        layout = QVBoxLayout()
        layout.addWidget(title)

        self.setLayout(layout)
