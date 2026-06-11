import os
import sys
from pathlib import Path
from PIL import Image

from PySide6 import QtCore 
from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent

from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QFileDialog, QSizePolicy, QMessageBox, QScrollArea,
    QStackedWidget
)


class LoadPage(QWidget):
    def __init__(self, main_window):
        super().__init__()

        self.main_window = main_window

        # Widgets
        self.image_drop_box = ImageDropBox(self.main_window)
        self.image_drop_box.setObjectName("imageDropBox")

        denoise_btn = QPushButton("Denoise Image")
        denoise_btn.setObjectName("denoiseButton")

        db_btn = QPushButton("Open file from Database")
        db_btn.setObjectName("dbButton")

        # Layouts
        btn_row = QHBoxLayout()
        btn_row.addWidget(denoise_btn)
        btn_row.addWidget(db_btn)
        

        main = QVBoxLayout(self)
        main.addWidget(self.image_drop_box)
        main.addLayout(btn_row)

        # Signals
        denoise_btn.clicked.connect(self.denoise_button)
        db_btn.clicked.connect(self.db_button)

    def denoise_button(self):
        if self.main_window.current_image is None:
            return

        self.main_window.show_denoise_page()
    
    def db_button(self):
        self.main_window.show_db_page()

class ImageDropBox(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)

        self.main_window = main_window
        self.file_path = None
        self.setObjectName("imageDropBox")

        self.setAcceptDrops(True)
        self.title_label = QLabel("drop your image here")
        self.subtitle_label = QLabel("or click to browse")

        self.title_label.setObjectName("uploadIconTitle")
        self.subtitle_label.setObjectName("uploadIconSubtitle")

        self.remove_btn = QPushButton("remove image")
        self.remove_btn.setVisible(False)
        self.remove_btn.clicked.connect(self.reset)

        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        layout.addStretch()
        layout.addWidget(self.title_label)
        layout.addWidget(self.subtitle_label)
        layout.addWidget(self.remove_btn)
        layout.addStretch()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.load_image()

    def load_image(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg *.bmp *.tif *.tiff)"
        )

        if path:
            self.set_image(path)
    
    def set_image(self, path):
        self.file_path = path

        image = Image.open(path).convert("RGB")
        self.main_window.current_image = image

        filename = os.path.basename(path)

        self.title_label.setText(filename)
        self.subtitle_label.setVisible(False)
        self.remove_btn.setVisible(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            self.setProperty("dragging", True)
            self.style().unpolish(self)
            self.style().polish(self)
            event.acceptProposedAction()

        print(self.property("dragging")) # debug remove later

    def dragLeaveEvent(self, event):
        self.setProperty("dragging", False)
        self.style().unpolish(self)
        self.style().polish(self)

    def dragMoveEvent(self, event):
        event.acceptProposedAction()
    
    def dropEvent(self, event):
        urls = event.mimeData().urls()

        if not urls:
            return
        
        path = urls[0].toLocalFile()

        if path.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")):
            self.set_image(path)

        self.setProperty("dragging", False)
        self.style().unpolish(self)
        self.style().polish(self)
    
    def reset(self):
        self.file_path = None
        self.main_window.current_image = None

        self.title_label.setText("drop the potato here") 
        self.subtitle_label.setText("or click to browse") # improve this or remove this redundancies

        self.remove_btn.setVisible(False)
        self.subtitle_label.setVisible(True)
        self.setProperty("dragging", False)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()
    
    def remove_image(self):
        if self.main_window.current_image is None:
            return

        self.image_drop_box.reset()
        