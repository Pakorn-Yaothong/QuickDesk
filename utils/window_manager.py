import pygetwindow as gw
import time

def move_window_exact(title_contains, x, y, w, h):
    """
    Move and resize a window to an exact screen position (in pixels).
    """
    for win in gw.getWindowsWithTitle(title_contains):
        try:
            win.restore()
            time.sleep(0.4)
            win.moveTo(x, y)
            win.resizeTo(w, h)
            break
        except:
            continue
