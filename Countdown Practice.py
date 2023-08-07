#this is a seconds timer to practice the time python library

import time

user_time = input("Welcome to the timer! Please enter how many seconds you want to time: ")
try:
    user_time = int(user_time)
except:
    while type(user_time) != int:
        user_time = input("please enter a valid number: ")
        try:
            user_time = int(user_time)
        except:
            continue

print("The timer is starting!")
while user_time > 0:
    print (user_time)
    user_time -= 1
    time.sleep(1)

if user_time == 0:
    print("The timer is done!")