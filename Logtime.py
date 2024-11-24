import time
import win32gui



#get active window
def get_active_window():
 
 window = win32gui.GetForegroundWindow() #current window encoded as int
 title = win32gui.GetWindowText(window) #turns int into string 


 return title #return title to main program




app_usage = {} #list that tracks app and app usage time
current_app =get_active_window() #current app being used
start_time = time.time() # start time



while True:
    new_app = get_active_window()
    if new_app != current_app:
        end_time = time.time()
        app_usage[current_app] = app_usage.get(current_app, 0) + (end_time - start_time)
        current_app = new_app
        print(current_app)
        print(app_usage)