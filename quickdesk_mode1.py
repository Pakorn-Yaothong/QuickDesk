from utils.app_launcher import launch_vscode, launch_chrome
from utils.window_manager import move_and_resize_window

def run_mode1(folder_path):
    launch_vscode(folder_path)
    launch_chrome(["https://www.youtube.com", "https://chat.openai.com"])

    move_and_resize_window("Visual Studio Code", target_display=0, align="right")
    move_and_resize_window("YouTube", target_display=0, align="left")
