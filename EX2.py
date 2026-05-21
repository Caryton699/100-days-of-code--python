 # Exercise 2 : Create a python program capable of greating you with Good morning ,Good afternoon ,Good evening and Good night. Your program should use time module to get the current hour.

#Solution:
import time

name = input("Enter your name: ")

hour= time.localtime().tm_hour
minute = time.localtime().tm_min
second = time.localtime().tm_sec

current = hour, minute, second

if hour < 12:
    print("Good morning!" , name ,"it's" , current)

elif hour < 18:
    print("Good afternoon!" , name ,"it's" , current)

elif hour < 21:
    print("Good evening!" , name ,"it's" , current)

else:
    print("Good night!" , name ,"it's" , current)