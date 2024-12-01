import time
import win32gui
import pprint
import copy

k =0

def main():
 
 current_app = get_active_window() #current app being used
 app_usage = {} #dictionary that tracks app usage
 start_time = time.time() # start time of programme
 app_counts = {}
 app_usage_last_word = {}
 app_usage_second_last_word = {}

 screentime(app_usage,start_time,current_app,app_counts, k,app_usage_last_word,app_usage_second_last_word)



#get active window
def get_active_window():
 
 window = win32gui.GetForegroundWindow() #current window encoded as int
 title = win32gui.GetWindowText(window) #turns int into string 


 return title if title.strip() else "Untitled Window" #handle empty titles


   



def screentime(app_usage,start_time,current_app, app_counts, k, app_usage_last_word, app_usage_second_last_word):

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
     
      app_usage_last_word = FormatData(app_usage)[0]
      app_usage_second_last_word = FormatData(app_usage)[1]

      print(f"Apps that have run:\n")
      pprint.pprint(app_usage) 
      print('\n')
      print("Amount of times app has run:\n")
      pprint.pprint(app_counts)
      print('\n')
      print("Formatted strings for further processing:\n")
      pprint.pprint(app_usage_last_word)
      print('\n')
      pprint.pprint(app_usage_second_last_word)


      print('-----------------------------')

      FormatData(app_usage)
      
     
#suspend program for 300ms to not overload CPU
      time.sleep(1)
 

#app switching logic
   elif new_app != current_app:
    
    app_counts[current_app] = app_counts[current_app] + 1 
   
    start_time = time.time()
    time.sleep(0.05)
    current_app = new_app





def FormatData(app_usage):
 
 second_last_string_array = []

 keys = list(app_usage.keys()) #getting list of apps
 last_string = [s.split("-")[-1] for s in keys] #last string in the list

 x = [t.split("-") for t in keys]

#conditions for apps with names shorter than 3 strings

 for list_of_strings in x: #gives a list of the strings in the bigger list
  
  if len(list_of_strings) == 2: 
   second_last_string = list_of_strings[0]

  elif len(list_of_strings) == 3:
   second_last_string = list_of_strings[1]

  elif len(list_of_strings) == 1:
   second_last_string = list_of_strings[0]

  second_last_string_array.append(second_last_string)

 
    
#getting rid of duplicates 
 no_dupes_last= list(set(last_string)) 
 no_dupes_second_last = list(set(second_last_string_array))

 return no_dupes_last, no_dupes_second_last





     
if __name__ == "__main__":
 main()