import time
import win32gui
import win32con
from screeninfo import get_monitors

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
    monitor = get_monitors()[0]  # จอหลัก
    return monitor.width, monitor.height

def move_window_exact(title_contains, x, y, w, h):
    time.sleep(0.5)
    hwnd = find_hwnd_by_title(title_contains)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        time.sleep(0.2)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, x, y, w, h,
                              win32con.SWP_NOZORDER | win32con.SWP_NOACTIVATE)
