from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QSizePolicy, QMessageBox, QScrollArea,
    QStackedWidget
)

class DBPage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        self.label = QLabel("database page where u should drop some delicacies")

        self.back_btn = QPushButton("Go Back")

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.back_btn)

        self.back_btn.clicked.connect(self.back_button)
        
    def back_button(self):
        self.main_window.denoised_image = None

        self.main_window.show_load_page()