from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout
)

class DashboardWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JobPilot AI - Dashboard")
        self.resize(900, 650)

        main_layout = QVBoxLayout()

        # Header Title
        header = QLabel("JobPilot AI Dashboard")
        header.setStyleSheet("font-size: 22px; font-weight: bold; margin-bottom: 10px;")
        main_layout.addWidget(header)

        # Navigation Bar Buttons
        nav_layout = QHBoxLayout()

        self.btn_resume = QPushButton("Resume Parser & ATS")
        self.btn_jobs = QPushButton("Job Matcher & Skill Gap")
        self.btn_profile = QPushButton("User Profile")

        nav_layout.addWidget(self.btn_resume)
        nav_layout.addWidget(self.btn_jobs)
        nav_layout.addWidget(self.btn_profile)

        main_layout.addLayout(nav_layout)

        # Placeholder Body View
        body_label = QLabel("Select a module above to get started.")
        body_label.setStyleSheet("font-size: 14px; color: #888; margin-top: 40px;")
        main_layout.addWidget(body_label)

        self.setLayout(main_layout)
        from resume import ResumeWindow
        self.btn_resume.clicked.connect(self.open_resume_module)
        def open_resume_module(self):
    self.resume_win = ResumeWindow()
    self.resume_win.show()
    git pull origin main
cd desktop
python main.py
        
    
        
        
        
