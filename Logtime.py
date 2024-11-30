import time
import win32gui
import pprint
import copy

k =1

def main():
 
 current_app = get_active_window() #current app being used
 app_usage = {} #dictionary that tracks app usage
 start_time = time.time() # start time of programme
 app_counts = {}
 app_usage_f = {}

 screentime(app_usage,start_time,current_app,app_counts, k,app_usage_f)



#get active window
def get_active_window():
 
 window = win32gui.GetForegroundWindow() #current window encoded as int
 title = win32gui.GetWindowText(window) #turns int into string 


 return title if title.strip() else "Untitled Window" #handle empty titles


def screentime(app_usage,start_time,current_app, app_counts, k, app_usage_f):

 while True:
   new_app = get_active_window()
   if new_app == current_app:
     #calculating elapsed time for current app
      elapsed_time_curr = time.time() - start_time

#add new app to dictionary with elapsed time if it doesnt already exist and increment timer
      app_usage[current_app] = app_usage.setdefault(current_app,elapsed_time_curr) 
      app_usage[current_app] = app_usage.get(current_app,0) + 1
     
     #add current app to app counter if not in already and set value to zero
      if current_app not in app_counts:
       app_counts[current_app] = app_usage.setdefault(current_app,0)
       app_counts[current_app] = 0
#print all the apps that have been running so far
    
      print(f"Apps that have run:\n")
      pprint.pprint(app_usage) 
      print("\n")
      pprint.pprint(app_counts)
      print('\n')
      print(app_usage_f)


      
     
#suspend program for 300ms to not overload CPU
      time.sleep(1)
 

#app switching logic
   elif new_app != current_app:
    
    app_counts[current_app] = app_counts[current_app] + 1 
   
    start_time = time.time()
    time.sleep(0.05)
    current_app = new_app




 
#def FormatData(app_usage):
 #app_usage_f = app_usage.keys()
 #screentime(app_usage_f)





     
if __name__ == "__main__":
 main()