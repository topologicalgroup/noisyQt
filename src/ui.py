# file for the ui
import sys

from pathlib import Path
from PySide6 import QtCore 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QSizePolicy, QMessageBox, QScrollArea,
)


class denoiseApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Denoiser")

        """# UI elements
        load_btn = QPushButton("Load Image")
        self.image_label = QLabel("No image loaded")

        # Layout
        btn_row = QHBoxLayout()
        btn_row.addWidget(load_btn)

        lbl_row = QHBoxLayout()
        lbl_row.addWidget(self.image_label)

        main = QVBoxLayout(self)
        main.addLayout(btn_row)
        main.addLayout(lbl_row)

        # Signals
        load_btn.clicked.connect(self.load_image)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)"""

        # Widgets
        load_btn = QPushButton("Load Image")

        self.image_label = QLabel("No image loaded")
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layouts
        btn_row = QHBoxLayout()
        btn_row.addWidget(load_btn)

        lbl_row = QHBoxLayout()
        lbl_row.addWidget(self.image_label)

        main = QVBoxLayout(self)

        main.addLayout(btn_row)
        main.addLayout(lbl_row)

        # Signals
        load_btn.clicked.connect(self.load_image)

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif *.tiff)"
        )

        self.image_label.setText(path)

def main():
    app = QApplication(sys.argv)
    w = denoiseApp(); w.resize(1100, 700); w.show()
    sys.exit(app.exec())

main()
