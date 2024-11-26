import time
import win32gui


#get active window
def get_active_window():
 
 window = win32gui.GetForegroundWindow() #current window encoded as int
 title = win32gui.GetWindowText(window) #turns int into string 


 return title if title.strip() else "Untitled Window" #handle empty titles

current_app = get_active_window() #current app being used
app_usage = {} #list that tracks app and app usage time
start_time = time.time() # start time of programme




while True:
  new_app = get_active_window()
  if new_app == current_app:
     time_step = time.time()
     elapsed_time = time_step - start_time
     print(elapsed_time)
     time.sleep(0.5)


     
 
    


    
