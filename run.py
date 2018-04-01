import random
import time
import subprocess
import psutil
import os
"""
Simple script to add responses to a simple Google form that only takes one number.

Go to your form page, and click Responses > Get pre-filled URL. It'll ask you to do a sample fill-out of your form. Put in responses that easily let you see what question you're answering. Once you hit submit, it's going to give you a URL in the form of...
https://docs.google.com/forms/d/<form_id>/viewform?entry.XXXXXXX=____&entry.YYYYYY=____...
set input to be this url as a string
"""
#Parameters: Change these in order to change affects of the program
default_browser = 'Google Chrome'
max_responses = 4000
max_wait_time = 500
min_wait_time = 1
input = "https://docs.google.com/forms/d/e/1FAIpQLSdKvDagIzG6E_3iYtwGs2RPR8T0luTzVVrZW1gyHhoXc0VBUg/viewform?usp=pp_url&entry.434085909=77"
#List is the skew of the randomness of the distribution.
#Place in list the numbers you want to appear more frequently in the form
#Out of the given number that you want to skew, list those you want to occur more often more times in list
#So if I want 7 and 77 to occur more often, but I want 7 to occur twice as often, list 7 twice and 77 once
list = [7, 7, 7, 7, 7, 7, 7, 7, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 77, 99, 9, 1, 100, 5, 11, 22, 33, 44, 55, 66, 77, 88, 7, 20, 18, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 4, 9, 16, 25, 36, 49, 64, 81, 100, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#In case the user entered the numbers in the wrong order
if min_wait_time > max_wait_time:
    min_wait_time, max_wait_time = max_wait_time, min_wait_time

#In case the user entered the same number twice
if min_wait_time == max_wait_time:
    max_wait_time = max_wait_time + 1

#remove the entered two-digit number from the end of the input
input = input[:-2]
#replace viewform with formResponse, the code used to create form responses
input = input.replace("viewform", "formResponse")

counter = 1
while counter <= max_responses:
    #Helps cause variation in submission time
    wait = random.randint(min_wait_time, max_wait_time)
    print("Waiting: " + str(wait) + " seconds")
    time.sleep(wait)
    
    num = random.randint(1, 100)
    if (counter%4 == 0 or counter%7 == 0 or counter%8 == 0 or counter%6 == 0):
        num = random.choice(list)
    try:
        print(num)
        output = input + str(num)
        b = subprocess.Popen(["/usr/bin/open", "/Applications/Google Chrome.app", output])
    except Exception as e:
            print(e)
            break
    time.sleep(2)
    for process in psutil.process_iter():
            name = process.name()
            if default_browser in name:
                os.kill(process.pid, 1)
    counter = counter + 1
