import pygetwindow as gw
import pyautogui
import time

def snap_window(title_contains, direction):
    """
    Snap window by partial title to left, right or maximize.
    - title_contains: string (part of window title)
    - direction: 'left', 'right', or 'maximize'
    """
    time.sleep(1)
    for w in gw.getWindowsWithTitle(title_contains):
        try:
            w.activate()
            time.sleep(0.3)
            if direction == 'left':
                pyautogui.hotkey('winleft', 'left')
            elif direction == 'right':
                pyautogui.hotkey('winleft', 'right')
            elif direction == 'maximize':
                pyautogui.hotkey('winleft', 'up')
            break
        except:
            continue
