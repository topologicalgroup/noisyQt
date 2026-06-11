"""
def main():
    print("Hello world")

if __name__ == "__main__":
    print("[INFO] Hi, This is a simple application that tests out image denoising using transformers.")
    # print([INFO] The model used comes from the paper "SwinIR: Image Restoration Using Swin Transformer" by Liang et al.")
    print("[INFO] https://arxiv.org/abs/2108.10257")
"""

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

from .pages.load_page import LoadPage
from .pages.denoise_page import DenoisePage
from .pages.db_page import DBPage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Denoiser")

        # Data shared
        self.current_image = None
        self.denoised_image = None

        # Pages
        self.stack = QStackedWidget()

        self.load_page = LoadPage(self)
        self.denoise_page = DenoisePage(self)
        self.db_page = DBPage(self)

        self.stack.addWidget(self.load_page)
        self.stack.addWidget(self.denoise_page)
        self.stack.addWidget(self.db_page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.show_load_page()


    def show_load_page(self):
        self.stack.setCurrentWidget(self.load_page)

    def show_denoise_page(self):
        self.stack.setCurrentWidget(self.denoise_page)
    
    def show_db_page(self):
        self.stack.setCurrentWidget(self.db_page)

if __name__ == "__main__":
    app = QApplication([])

    qss_path = Path(__file__).parent / "styles" / "app.qss"
    with open(qss_path, "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    app.exec()
