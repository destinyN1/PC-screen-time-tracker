import time
import win32gui
import pprint


#get active window
def get_active_window():
 
 window = win32gui.GetForegroundWindow() #current window encoded as int
 title = win32gui.GetWindowText(window) #turns int into string 


 return title if title.strip() else "Untitled Window" #handle empty titles

current_app = get_active_window() #current app being used
app_usage = {} #dictionary that tracks app usage
start_time = time.time() # start time of programme




while True:
  new_app = get_active_window()
  if new_app == current_app:
     
     time_step_curr = time.time()
     elapsed_time_curr = time_step_curr - start_time

     app_usage[current_app] = app_usage.setdefault(current_app,elapsed_time_curr)
     app_usage[current_app] = elapsed_time_curr

     print(f"elapsed time curr:\n")
     pprint.pprint(app_usage)
     
     time.sleep(1)
     new_app = current_app

  elif new_app != current_app:
    time_step_new = time.time()
    elapsed_time_new = time_step_new - start_time
    print(f"elapsed time new: {elapsed_time_new}, {current_app}")
    time.sleep(0.5)
    current_app = new_app


  


     
 
    


    
