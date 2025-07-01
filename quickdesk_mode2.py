# quickdesk_mode2.py

from utils.app_launcher import launch_vscode, launch_chrome, launch_discord
from utils.window_manager import snap_window

def run_mode2_1(folder_path):
    """
    Mode 2.1:
    - Main Display: VSCode
    - Second Display: Chrome with ChatGPT (left) and YouTube (right)
    """
    launch_vscode(folder_path)
    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])

    snap_window("Visual Studio Code", "maximize")
    snap_window("ChatGPT", "left")
    snap_window("YouTube", "right")

def run_mode2_2(folder_path):
    """
    Mode 2.2:
    - Main Display: Chrome (ChatGPT left) + VSCode (right)
    - Second Display: Discord fullscreen
    """
    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])
    snap_window("ChatGPT", "left")

    launch_vscode(folder_path)
    snap_window("Visual Studio Code", "right")

    launch_discord()
    snap_window("Discord", "maximize")
