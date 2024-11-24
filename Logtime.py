import time
import win32gui



#get active window
def get_active_window():
 
 window = win32gui.GetForegroundWindow() #current window encoded as int
 title = win32gui.GetWindowText(window) #turns int into string 


 return title #return title to main program

current_app = get_active_window() #current app being used


app_usage = {} #list that tracks app and app usage time
start_time = time.time() # start time

while True:
    new_app = get_active_window() #next application
    if new_app != current_app:
        end_time = time.time()
        curr_run_time = end_time - start_time
        app_usage[current_app] = app_usage.get(current_app, 0)  + (curr_run_time) #adding timer field at the end
        x = app_usage.values()       
        print(x)
        print(app_usage)
        current_app = new_app
        time.sleep(1)

    
