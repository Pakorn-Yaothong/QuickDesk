import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog,
    QMessageBox, QComboBox, QLabel, QHBoxLayout
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from quickdesk_mode1 import run_mode1
from quickdesk_mode2 import run_mode2_1, run_mode2_2

class QuickDeskMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickDesk Launcher")
        self.setFixedSize(420, 260)
        self.setWindowIcon(QIcon("assets/quickdesk_icon.ico"))  # ตั้งไอคอนแบบกำหนดเอง

        self.selected_folder = None

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignTop)

        title = QLabel("🚀 Launch Your Workspace Faster!")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin-bottom: 12px;")
        main_layout.addWidget(title)

        self.mode_combo = QComboBox()
        self.mode_combo.addItems([
            "Mode 1 (Single Display)",
            "Mode 2.1 (2 Displays - VSCode on Main)",
            "Mode 2.2 (2 Displays - Chrome on Main)"
        ])
        self.mode_combo.setStyleSheet("padding: 6px; font-size: 14px;")
        main_layout.addWidget(QLabel("Choose Mode:"))
        main_layout.addWidget(self.mode_combo)

        self.folder_btn = QPushButton("📂 Select Folder for VSCode")
        self.folder_btn.clicked.connect(self.select_folder)
        self.folder_btn.setStyleSheet("padding: 8px; font-size: 14px;")
        main_layout.addWidget(self.folder_btn)

        self.launch_btn = QPushButton("🚀 Launch QuickDesk")
        self.launch_btn.clicked.connect(self.run_mode)
        self.launch_btn.setStyleSheet(
            "padding: 10px; font-size: 16px; background-color: #4CAF50; color: white;"
        )
        main_layout.addWidget(self.launch_btn)

        self.setLayout(main_layout)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.selected_folder = folder

    def run_mode(self):
        if not self.selected_folder:
            QMessageBox.warning(self, "No folder selected", "Please select a folder first.")
            return

        mode = self.mode_combo.currentIndex()

        if mode == 0:
            run_mode1(self.selected_folder)
        elif mode == 1:
            run_mode2_1(self.selected_folder)
        elif mode == 2:
            run_mode2_2(self.selected_folder)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QuickDeskMain()
    win.setWindowFlags(win.windowFlags() & ~Qt.WindowContextHelpButtonHint)  
    win.show()
    sys.exit(app.exec_())
