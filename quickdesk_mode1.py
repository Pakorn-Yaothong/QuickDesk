# quickdesk_mode1.py

from utils.app_launcher import launch_vscode, launch_chrome
from utils.window_manager import snap_window

def run_mode1(folder_path):
    """
    Logic for Mode 1 (1 Display):
    - Launch VSCode with selected folder
    - Launch Chrome with YouTube + ChatGPT
    - Snap VSCode to right, Chrome (YouTube) to left
    """
    launch_vscode(folder_path)
    launch_chrome(["https://www.youtube.com", "https://chat.openai.com"])
    snap_window("Visual Studio Code", "right")
    snap_window("YouTube", "left")
