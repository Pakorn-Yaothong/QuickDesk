from screeninfo import get_monitors
import pygetwindow as gw
import time

def get_display_positions():
    """Return list of (x, y, width, height) for all monitors"""
    return [(m.x, m.y, m.width, m.height) for m in get_monitors()]

def move_and_resize_window(title_contains, target_display=0, align="left"):
    """
    Move & resize a window to specific display + alignment.
    align: 'left', 'right', or 'maximize'
    """
    positions = get_display_positions()
    if target_display >= len(positions):
        return

    x, y, w, h = positions[target_display]

    for win in gw.getWindowsWithTitle(title_contains):
        try:
            win.restore()
            time.sleep(0.3)
            if align == "left":
                win.moveTo(x, y)
                win.resizeTo(w // 2, h)
            elif align == "right":
                win.moveTo(x + w // 2, y)
                win.resizeTo(w // 2, h)
            elif align == "maximize":
                win.moveTo(x, y)
                win.resizeTo(w, h)
            break
        except:
            continue
