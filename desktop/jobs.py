import sys
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QLineEdit, QTextEdit, QMessageBox
)

class JobsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JobPilot AI - Job Matcher & Skill Gap Analyzer")
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Title Header
        title = QLabel("Job Matcher & Skill Gap Analysis")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        # Job Description Input
        self.job_title_input = QLineEdit()
        self.job_title_input.setPlaceholderText("Target Job Title (e.g., Python Developer)")
        layout.addWidget(self.job_title_input)

        self.jd_input = QTextEdit()
        self.jd_input.setPlaceholderText("Paste Job Description (JD) here...")
        layout.addWidget(self.jd_input)

        # Analyze Match Button
        self.match_btn = QPushButton("Analyze Job Match & Gaps")
        self.match_btn.clicked.connect(self.analyze_match)
        layout.addWidget(self.match_btn)

        self.setLayout(layout)

    def analyze_match(self):
        job_title = self.job_title_input.text()
        jd_text = self.jd_input.toPlainText()

        if not job_title or not jd_text:
            QMessageBox.warning(self, "Warning", "Please enter both a Job Title and Job Description.")
        else:
            QMessageBox.information(
                self, 
                "Job Match Result", 
                f"Job Title: {job_title}\nMatch Percentage: 78%\n\nMissing Skills identified: Docker, PostgreSQL, REST APIs"
      )
      
