# quickdesk_main.py

import sys
import subprocess
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog,
    QMessageBox, QComboBox, QLabel
)

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
        self.start_btn.clicked.connect(self.run_mode)

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
        QMessageBox.information(
            self,
            "QuickDesk",
            f"Selected mode: {self.mode_combo.currentText()}\nFolder: {self.selected_folder or 'Not selected'}"
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QuickDeskMain()
    win.show()
    sys.exit(app.exec_())
