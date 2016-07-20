##Importing Python's time module to allow for timed pauses
import time

##Defining the askName variable
askName = input ("Oh, hey. What's your name? ")
##askName value is now stored so we can invoke it below

##I just love it when computers use casual language. But why is there an extra space when askName gets printed?
print ("\n\nHi there,", askName, ". It's great to meet you.")

##waiting for input
input ("\n\nWell, that's about all I have time for at the moment. Press the Enter key to exit this program.")
print ("\n\nExiting program. Byyye!")

##Pausing for one second to say goodbye because it's good HCI
time.sleep(1)

