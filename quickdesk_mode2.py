from utils.app_launcher import launch_vscode, launch_chrome, launch_discord
from utils.window_manager import move_and_resize_window

def run_mode2_1(folder_path):
    launch_vscode(folder_path)
    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])

    move_and_resize_window("Visual Studio Code", target_display=0, align="maximize")
    move_and_resize_window("ChatGPT", target_display=1, align="left")
    move_and_resize_window("YouTube", target_display=1, align="right")

def run_mode2_2(folder_path):
    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])
    move_and_resize_window("ChatGPT", target_display=0, align="left")

    launch_vscode(folder_path)
    move_and_resize_window("Visual Studio Code", target_display=0, align="right")

    launch_discord()
    move_and_resize_window("Discord", target_display=1, align="maximize")
