# quickdesk_mode1.py

from utils.app_launcher import launch_vscode, launch_chrome
from utils.window_manager import move_window_exact
import time

def run_mode1(folder_path):
    launch_vscode(folder_path)
    launch_chrome(["https://www.youtube.com", "https://chat.openai.com"])

    time.sleep(3)

    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    TASKBAR_HEIGHT = 48
    HEIGHT = SCREEN_HEIGHT - TASKBAR_HEIGHT

    move_window_exact("Google Chrome", -5, 0, int(973.5), int(HEIGHT + 7))
    move_window_exact("Visual Studio Code", 960, 0, 950, HEIGHT)
