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

from pages.load_page import loadPage
from pages.denoise_page import denoisePage


class mainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Denoiser")

        # Data shared
        self.current_image = None
        self.denoised_image = None

        # Pages
        self.stack = QStackedWidget()

        self.load_page = loadPage(self)
        self.denoise_page = denoisePage(self)

        self.stack.addWidget(self.load_page)
        self.stack.addWidget(self.denoise_page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stack)

        self.show_load_page()


    def show_load_page(self):
        self.stack.setCurrentWidget(self.load_page)

    def show_denoise_page(self):
        self.stack.setCurrentWidget(self.denoise_page)

app = QApplication([])
window = mainWindow()
window.show()
app.exec()