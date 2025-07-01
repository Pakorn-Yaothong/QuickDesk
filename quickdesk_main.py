import sys
import subprocess
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog,
    QMessageBox, QComboBox, QLabel
)

from quickdesk_mode1 import run_mode1  # ✅ import ครั้งเดียวพอ

class QuickDeskMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuickDesk Launcher")
        self.setFixedSize(400, 250)

        layout = QVBoxLayout()

        # Dropdown for mode selection
        self.mode_combo = QComboBox()
        self.mode_combo.addItems([
            "Mode 1 (1 Display)", 
            "Mode 2.1 (2 Displays - VSCode on Main)",
            "Mode 2.2 (2 Displays - VSCode on Second)"
        ])

        # Folder selection button
        self.folder_btn = QPushButton("Select Folder for VSCode")
        self.folder_btn.clicked.connect(self.select_folder)

        # Execute button
        self.start_btn = QPushButton("Launch QuickDesk")
        self.start_btn.clicked.connect(self.run_mode)  # ✅ เชื่อมกับของจริง

        layout.addWidget(QLabel("Select a mode:"))
        layout.addWidget(self.mode_combo)
        layout.addWidget(self.folder_btn)
        layout.addWidget(self.start_btn)

        self.setLayout(layout)
        self.selected_folder = None

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select a folder")
        if folder:
            self.selected_folder = folder

    def run_mode(self):
        if not self.selected_folder:
            QMessageBox.warning(self, "No folder", "Please select a folder first.")
            return

        mode_index = self.mode_combo.currentIndex()
        
        if mode_index == 0:  # Mode 1
            run_mode1(self.selected_folder)
        else:
            QMessageBox.information(
                self,
                "Coming Soon",
                "This mode is not implemented yet."
            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QuickDeskMain()
    win.show()
    sys.exit(app.exec_())
