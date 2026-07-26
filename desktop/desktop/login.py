from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("JobPilot AI")
        self.resize(400, 500)

        title = QLabel("JobPilot AI")
        title.setStyleSheet("font-size:28px;font-weight:bold;")

        subtitle = QLabel("Your AI Career Navigator")

        self.email = QLineEdit()
        self.email.setPlaceholderText("Email")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Password")
        self.password.setEchoMode(QLineEdit.Password)

        button = QPushButton("Login")
        button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addWidget(self.email)
        layout.addWidget(self.password)
        layout.addWidget(button)

        self.setLayout(layout)

    def login(self):
        QMessageBox.information(
            self,
            "Success",
            "Welcome to JobPilot AI!"
        )
