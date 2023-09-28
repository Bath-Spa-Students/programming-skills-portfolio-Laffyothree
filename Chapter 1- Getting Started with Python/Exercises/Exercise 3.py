from datetime import date 
today = date.today()
print ("The date today is: ", today)

import time 
curr_time = time.strftime("%H:%M:%S", time.localtime())
print("The current time is: ", curr_time)