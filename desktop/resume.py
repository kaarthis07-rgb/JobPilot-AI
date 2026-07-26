import sys
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QFileDialog, QTextEdit, QMessageBox
)

class ResumeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JobPilot AI - Resume Parser & ATS")
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Title Header
        title = QLabel("Resume Parser & ATS Score")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        # File Upload Section
        file_layout = QHBoxLayout()
        self.upload_btn = QPushButton("Upload Resume (PDF)")
        self.upload_btn.clicked.connect(self.upload_resume)
        self.file_label = QLabel("No file selected")
        
        file_layout.addWidget(self.upload_btn)
        file_layout.addWidget(self.file_label)
        layout.addLayout(file_layout)

        # Extracted Text Display Area
        self.text_display = QTextEdit()
        self.text_display.setPlaceholderText("Parsed resume content will appear here...")
        layout.addWidget(self.text_display)

        # Analyze Button
        self.analyze_btn = QPushButton("Analyze ATS Score")
        self.analyze_btn.clicked.connect(self.analyze_resume)
        layout.addWidget(self.analyze_btn)

        self.setLayout(layout)

    def upload_resume(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Resume", "", "PDF Files (*.pdf);;Text Files (*.txt)"
        )
        if file_path:
            self.file_label.setText(file_path.split("/")[-1])
            self.text_display.setText(f"File loaded successfully: {file_path}")

    def analyze_resume(self):
        if self.file_label.text() == "No file selected":
            QMessageBox.warning(self, "Warning", "Please upload a resume first.")
        else:
            QMessageBox.information(self, "ATS Analysis", "ATS Match Score: 85%\n\nTop Skills Found: Python, PySide6, AI Development")
      
