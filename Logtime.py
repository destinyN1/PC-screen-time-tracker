import time
import win32gui
import pprint
from datetime import datetime, timezone
from DataBase import init_db, update_db
import json



last_active = {} #when was the app last active
first_active = {} #when was the app first active
app_usage = {} #dictionary that tracks app usage
start_time = time.time() # start time of programme
app_counts = {} #how many times has has the app been opened

#main program and sub program
app_usage_last_word = {}
app_usage_second_last_word = {}


def main():
 current_app = get_active_window() #current app being used


 screentime(current_app,start_time)



#get active window
def get_active_window():
 
 window = win32gui.GetForegroundWindow() #current window encoded as int
 title = win32gui.GetWindowText(window) #turns int into string 

 return title if title.strip() else "Untitled Window" #handle empty titles



def screentime(current_app,start_time):

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

      #Get the last word and second last word from title string     
      app_usage_last_word = FormatData(app_usage)[0]
      app_usage_second_last_word = FormatData(app_usage)[1]
      
      #Last time an app was active
      last_active = LastSession(app_usage,current_app)
      first_active = FirstSesion(current_app)
      

    
  
      #print for debugging 
      printf(app_usage, app_counts, app_usage_last_word,app_usage_second_last_word,last_active,first_active)


      last_string = FormatData(app_usage)[3]
      second_last_string = FormatData(app_usage)[2]

      ToJson(current_app, last_string, second_last_string)
 

            
#suspend program for 1000ms to not overload CPU
      time.sleep(1)
 
#app switching logic
   elif new_app != current_app:
    
    #counting times current app has been switched
    app_counts[current_app] = app_counts[current_app] + 1 



    start_time = time.time()
    time.sleep(0.05)
    current_app = new_app


#getting the last time from when an app was active
def LastSession(app_usage,current_app):
 
 logtime = str(datetime.now(timezone.utc))
 last_active[current_app] = app_usage.setdefault(current_app,logtime)
 last_active.update({current_app:logtime})
 
 return last_active


#getting first time an app has been opened
def FirstSesion(current_app):
 
 logtime = str(datetime.now(timezone.utc))

 if current_app not in first_active:
  first_active[current_app] = logtime


 return first_active


#formatting data to extract main program and sub program
def FormatData(app_usage):
 
 second_last_string_array = []

 keys = list(app_usage.keys()) #getting list of apps
 last_string = [s.split("-")[-1] for s in keys] #last string in the list
 
 last_string = last_string[0]

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
 no_dupes_last_list= list(set(last_string)) 
 no_dupes_second_last_list = list(set(second_last_string_array))


 return no_dupes_last_list, no_dupes_second_last_list, second_last_string, last_string


def printf(app_usage, app_counts, app_usage_last_word,app_usage_second_last_word,last_active,first_active):
  print(f"Apps that have run:\n")
  safe_pprint.pprint(app_usage) 
  print('\n')
  print("Amount of times app has run:\n")
  safe_pprint.pprint(app_counts)
  print('\n')
  print("Main Program:\n")
  safe_pprint.pprint(app_usage_last_word)
  print('\n')
  print("Sub program: \n")
  safe_pprint.pprint(app_usage_second_last_word)
  print('\n')
  print("Last time an app was active:\n")
  safe_pprint.pprint(last_active)
  print('\n')
  print("First time an app was active:\n")
  safe_pprint.pprint(first_active)
  print('-----------------------------')

#converts the current app's parameters into a JSON dictionary file
def ToJson(current_app, last_string, second_last_string):
 
 per_appdata ={
   
    "window": current_app,  
    "main app": last_string,
    "sub app": second_last_string,
    "total_duration": app_usage[current_app],
    "first active": first_active[current_app],
    "last active": last_active[current_app],
    "times opened": app_counts[current_app]
}

 per_appdata_json= json.dumps(per_appdata, indent = 4 ) 

 print(per_appdata_json)

#Handles titles that dont have standard ASCII values
class SafePrettyPrinter(pprint.PrettyPrinter):
    def format(self, obj, context, maxlevels, level):
        if isinstance(obj, str):
            obj = obj.encode('ascii', 'replace').decode('ascii')  # Replace unsupported characters
        return super().format(obj, context, maxlevels, level)

# Instantiate SafePrettyPrinter
safe_pprint = SafePrettyPrinter() 

     
if __name__ == "__main__":
 #init_db()
 main()