from utils.app_launcher import launch_vscode, launch_chrome, launch_discord
from utils.window_manager import move_window_exact  
import time

def run_mode2_1(folder_path):
    launch_vscode(folder_path)
    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])
    time.sleep(3.0)

    # จอหลัก
    move_window_exact("Visual Studio Code", 0, 0, 1920, 1080)

    # จอรอง (x เริ่มที่ 1920)
    move_window_exact("Google Chrome", 1920, 0, 960, 1080)         # ฝั่งซ้าย
    move_window_exact("YouTube", 1920 + 960, 0, 960, 1080)         # ฝั่งขวา

def run_mode2_2(folder_path):
    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])
    time.sleep(3.0)

    # จอหลัก
    move_window_exact("Google Chrome", 0, 0, 970, 1080)
    launch_vscode(folder_path)
    move_window_exact("Visual Studio Code", 960, 0, 960, 1080)

    # จอรอง
    launch_discord()
    move_window_exact("Discord", 1920, 0, 1920, 1080)
