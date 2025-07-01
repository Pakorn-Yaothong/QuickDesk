from utils.app_launcher import launch_vscode, launch_chrome
from utils.window_manager import move_window_exact  
import time

def run_mode1(folder_path):
    launch_vscode(folder_path)
    launch_chrome(["https://www.youtube.com", "https://chat.openai.com"])

    time.sleep(3.0)

    # หน้าจอหลัก 1920x1080
    move_window_exact("Google Chrome", 0, 0, 970, 1080)
    move_window_exact("Visual Studio Code", 960, 0, 960, 1080)
