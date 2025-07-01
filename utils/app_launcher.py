# utils/app_launcher.py

import subprocess
import os
from PyQt5.QtWidgets import QMessageBox

def launch_vscode(path):
    try:
        if not path or not os.path.exists(path):
            raise FileNotFoundError("Invalid path to open VSCode.")
        
        vscode_path = r"C:\Users\foxve\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        subprocess.Popen([vscode_path, path])
    except Exception as e:
        QMessageBox.critical(None, "VSCode Not Found", f"Cannot open VSCode:\n{e}")



def launch_chrome(urls):
    try:
        chrome_path = r"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        subprocess.Popen([chrome_path, "--new-window"] + urls)
    except FileNotFoundError:
        QMessageBox.critical(None, "Chrome Not Found", "Google Chrome is not installed.")

def launch_discord():
    try:
        discord_path = os.path.expandvars(r"%LOCALAPPDATA%\\Discord\\Update.exe")
        subprocess.Popen([discord_path, "--processStart", "Discord.exe"])
    except Exception:
        QMessageBox.critical(None, "Discord Not Found", "Discord is not installed or failed to launch.")
