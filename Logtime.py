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
     
     #calculating elapsed time for current app
     time_step_curr = time.time()
     elapsed_time_curr = time_step_curr - start_time
#add new app to dictionary with elapsed time if it doesnt already exist and increment timer
     app_usage[current_app] = app_usage.setdefault(current_app,elapsed_time_curr) 
     app_usage[current_app] = elapsed_time_curr 

#print all the apps that have been running so far
     print(f"Apps that have run:\n")
     pprint.pprint(app_usage) 

#suspend program for 500ms to not overload CPU
     time.sleep(0.5)
     new_app = current_app

  elif new_app != current_app:
    time_step_new = time.time()
    elapsed_time_new = time_step_new - start_time
    print(f"elapsed time new: {elapsed_time_new}, {current_app}")
    time.sleep(0.5)
    current_app = new_app


  


     
 
    


    
