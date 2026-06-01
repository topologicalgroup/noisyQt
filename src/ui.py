# file for the ui
import sys

from PySide6 import QtCore
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QSizePolicy, QMessageBox, QScrollArea,
)


class denoiseApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Denoiser")

        self.text = QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.text)

def main():
    app = QApplication(sys.argv)
    w = denoiseApp(); w.resize(1100, 700); w.show()
    sys.exit(app.exec())

main()
