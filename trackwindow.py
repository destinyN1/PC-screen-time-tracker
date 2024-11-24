from win32gui import GetWindowText, GetForegroundWindow
import win32gui

def get_active_window():
 
 window = win32gui.GetForegroundWindow()
 title = win32gui.GetWindowText(window)


 return title


get_active_window() 