import sys
from pathlib import Path
from PIL import Image

from PySide6 import QtCore 
from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QSizePolicy, QMessageBox, QScrollArea,
    QStackedWidget
)

class loadPage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        # Widgets
        self.image_label = QLabel("No image loaded")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        upload_btn = QPushButton("Upload Image")
        denoise_btn = QPushButton("Denoise Image")
        remove_image_btn = QPushButton("Remove Image")

        # Layouts
        btn_row = QHBoxLayout()
        btn_row.addWidget(upload_btn)
        btn_row.addWidget(denoise_btn)
        btn_row.addWidget(remove_image_btn)
        

        main = QVBoxLayout(self)

        main.addWidget(self.image_label)
        main.addLayout(btn_row)

        # Signals
        upload_btn.clicked.connect(self.load_image)
        denoise_btn.clicked.connect(self.denoise_button)
        remove_image_btn.clicked.connect(self.remove_image)

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif *.tiff)"
        )
        if not path:
            return
        image = Image.open(path).convert("RGB")
        self.main_window.current_image = image 
        # i put this here for changing pages reason*
        
        print(self.main_window.current_image)
        self.image_label.setText(path)

    def denoise_button(self):
        if self.main_window.current_image is None:
            return

        self.main_window.show_denoise_page()
    
    def remove_image(self):
        if self.main_window.current_image is None:
            return

        self.main_window.current_image = None
        self.image_label.setText("No image loaded")