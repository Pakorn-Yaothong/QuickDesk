# utils/window_manager.py

import time
import win32gui
import win32con
from screeninfo import get_monitors
from PyQt5.QtWidgets import QMessageBox

def find_hwnd_by_title(partial_title):
    def enum_callback(hwnd, result):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if partial_title.lower() in title.lower():
                result.append(hwnd)
    result = []
    win32gui.EnumWindows(enum_callback, result)
    return result[0] if result else None

def get_main_screen_size():
    monitor = get_monitors()[0]  # main display
    return monitor.width, monitor.height

def move_window_exact(title_contains, x, y, w, h):
    time.sleep(0.5)
    hwnd = find_hwnd_by_title(title_contains)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(0.2)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, w, h,
                              win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE)

def get_all_screen_sizes():
    monitors = get_monitors()
    return [{"x": m.x, "y": m.y, "width": m.width, "height": m.height} for m in monitors]

def show_warning(message):
    QMessageBox.warning(None, "Display Error", message)

def get_all_screen_sizes():
    monitors = get_monitors()
    return [{"x": m.x, "y": m.y, "width": m.width, "height": m.height} for m in monitors]

def show_warning(message):
    QMessageBox.warning(None, "Display Error", message)

def get_display_offset(index=1):
    monitors = get_monitors()
    if len(monitors) > index:
        monitor = monitors[index]
        return monitor.x, monitor.y
    return 0, 0

from screeninfo import get_monitors

def get_secondary_screen_size():
    monitors = get_monitors()
    if len(monitors) > 1:
        second = monitors[1]  # second display  (index 1)
        return second.width, second.height
    return 0, 0  # fallback: no second display
