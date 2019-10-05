import win32gui
import win32con
import win32api

hwnd = win32gui.FindWindow(None, "Overlay")
posX, posY, width, height = win32gui.GetWindowPlacement(hwnd)[4]

windowStyles = win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, windowStyles)
win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, posX,posY, 0,0, win32con.SWP_NOSIZE)

windowAlpha = 180
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0),
windowAlpha, win32con.LWA_ALPHA)