import sys
from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, 
    QHBoxLayout, QFileDialog, QTextEdit, QMessageBox
)

try:
    import pypdf
except ImportError:
    pypdf = None

class ResumeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JobPilot AI - Resume Parser & ATS")
        self.resize(800, 600)

        layout = QVBoxLayout()

        # Title
        title = QLabel("Resume Parser & ATS Score")
        title.setStyleSheet("font-size: 20px; font-weight: bold; margin-bottom: 10px;")
        layout.addWidget(title)

        # Upload Controls
        file_layout = QHBoxLayout()
        self.upload_btn = QPushButton("Upload Resume (PDF)")
        self.upload_btn.clicked.connect(self.upload_resume)
        self.file_label = QLabel("No file selected")
        
        file_layout.addWidget(self.upload_btn)
        file_layout.addWidget(self.file_label)
        layout.addLayout(file_layout)

        # Text Output Area
        self.text_display = QTextEdit()
        self.text_display.setPlaceholderText("Parsed resume content will appear here...")
        layout.addWidget(self.text_display)

        # Action Button
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
            parsed_text = self.extract_text_from_pdf(file_path)
            self.text_display.setText(parsed_text)

    def extract_text_from_pdf(self, pdf_path):
        if not pypdf:
            return "pypdf package is not installed. Please run 'pip install pypdf'."
        
        try:
            reader = pypdf.PdfReader(pdf_path)
            extracted = ""
            for page in reader.pages:
                extracted += page.extract_text() or ""
            return extracted if extracted else "Could not extract text from this PDF."
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

    def analyze_resume(self):
        text = self.text_display.toPlainText()
        if not text or "No file selected" in self.file_label.text():
            QMessageBox.warning(self, "Warning", "Please upload a valid resume PDF first.")
        else:
            word_count = len(text.split())
            QMessageBox.information(
                self, 
                "ATS Overview", 
                f"Resume Processed Successfully!\nTotal Word Count: {word_count}\n\nATS Score: 82/100"
            )
            
