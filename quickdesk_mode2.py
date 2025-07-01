# quickdesk_mode2.py

import time
from utils.app_launcher import launch_vscode, launch_chrome, launch_discord
from utils.window_manager import (
    move_window_exact, get_main_screen_size,
    get_secondary_screen_size, show_warning
)

TASKBAR_HEIGHT = 48

def run_mode2_1(folder_path):
    main_width, HEIGHT = get_main_screen_size()
    second_width, second_height = get_secondary_screen_size()

    if second_width == 0:
        show_warning("Only one display detected. Mode 2 requires two displays.")
        return

    launch_vscode(folder_path)
    time.sleep(1)
    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])
    time.sleep(2)
    launch_discord()

    # Main display: VSCode fullscreen
    move_window_exact("Visual Studio Code", 0, 0, main_width, HEIGHT)

    # Display 2 (right side): Chrome on left / Discord on right
    move_window_exact("Google Chrome", main_width - 5, 0, int(973.5), int(HEIGHT + 7))
    move_window_exact("Discord", main_width + 960, 0, 960, HEIGHT)


def run_mode2_2(folder_path):
    main_width, SCREEN_HEIGHT = get_main_screen_size()
    second_width, second_height = get_secondary_screen_size()
    HEIGHT = SCREEN_HEIGHT - TASKBAR_HEIGHT

    if second_width == 0:
        show_warning("Only one display detected. Mode 2 requires two displays.")
        return

    launch_chrome(["https://chat.openai.com", "https://www.youtube.com"])
    time.sleep(1)
    launch_vscode(folder_path)
    time.sleep(2)
    launch_discord()

    # ✅ Main Display: Chrome 35% / VSCode 65%
    chrome_width = int(main_width * 0.35)
    vscode_width = main_width - chrome_width

    move_window_exact("Google Chrome", -5, 0, int(chrome_width + 14), int(HEIGHT + 7))
    move_window_exact("Visual Studio Code", chrome_width, 0, vscode_width, HEIGHT)

    # ✅ Display 2: Discord full screen
    move_window_exact("Discord", main_width, 0, second_width, second_height)


