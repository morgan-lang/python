#Program name: number-crunch-o-matic.py
#Program function: to perform simple arithmetic on user-entered data
#Author: Morgan Lang
#Date modified: 06/28/2016
#################################################################


#First, we'll import the time module so we can control the timing of steps
import time

#Program introduction & credits using backslashes to demonstrate escape characters.
print ("\t\t\t \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print ("\t\t\tSuper Amazing Number Crunch-O-Matic")
print ("\t\t\t \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
print ("\t\t\t\t\tby")
print ("\t\t\t\tMorgan Lang")
print ("\t\t\t \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\ \\")
time.sleep(1)

#Although it's totally unnecessary for the purposes of this class, I believe that pacing is an important part of interactivity. This section creates the illusion of beginning the "real" part of the program and helps provide structure to the user.
print ("\n\n")
print ("\n\nHang on a sec.")
time.sleep(1)
print ("\nOK. Beginning program...")

#Assigning the return value of the input function to a variable named askNumber1. 
askNumber1 = input("\nAll righty, then. Let's perform some simple arithmetic on two numbers. \nTo start, give me a number. You can use decimals and negative numbers. ")
time.sleep(1)
print ("\nOK. You entered", askNumber1, ". That's great. Now I'd like you to enter another number. ")

#Assigning the return value of another input function to a variable named askNumber2
askNumber2 = input("\nEnter a second number, please. ")
time.sleep(1)
print ("\nGreat. You entered", askNumber2, " . Now I'm going to add these two numbers. Hang on while I think for a sec.")

#Pausing for dramatic effect
time.sleep(1)

#This next step redefines the return values of askNumber1 and askNumber2 as floating point numbers. This step is necessary in order to perform mathematical operations, because values obtained using input() are, by default, strings. Attempting to perform addition on strings will concatenate them rather than add them.

#Note that this step wouldn't be necessary if I had defined the return values for askNumber1 and askNumber2 as floats when I first assigned values. For example: 
#askNumber1=float(input("\nAll righty, then. Let's add two numbers. To start, give me a number. "))

#Redefining the return values of askNumber1 and askNumber2 as floats:
x = float(askNumber1)
y = float(askNumber2)

#Addition
print ("\nOK, got it. The sum of ", x, "and ", y, "is ", x+y,".")
time.sleep(1)

#Subtraction
print ("\nNow I'm going to subtract", y, "from", x, ". ", "Hang on while I think for a sec.")
time.sleep(2)
print ("\nOK, got it.", x, " minus", y, "is ", x-y,".")
time.sleep(1)

#Multiplication
print ("\nNow I'm going to multiply", y, "and", x, ". ", "Hang on while I think for a sec.")
time.sleep(2)
print ("\nOK, got it.", x, " multiplied by", y, "is ", x*y, ".")
time.sleep(1)

#Division
print ("\nNow I'm going to divide", y, "by", x, ". ", "Hang on while I think for a sec.")
time.sleep(2)
print ("\nOK, got it.", y, " divided by", x, "is ", y/x,".")
time.sleep(1)

#Division
print ("\nFinally, let's find the average of", x, "and", y, ". ", "Hang on while I think for a sec.")
time.sleep(2)
print ("\nOK, got it. The average of", x, " and", y, "is ", (x+y)/2,".")
time.sleep(1)

#Exit prompt
input ("\nWe should totally do this again sometime. \nFor now, press the Enter key to quit this program.")

#Ring system bell when user responds
print("\a")

#Show some snazzy ASCII art for 2 seconds using blockquotes
print (
   """


  ____             _ 
 |  _ \           | |
 | |_) |_   _  ___| |
 |  _ <| | | |/ _ \ |
 | |_) | |_| |  __/_|
 |____/ \__, |\___(_)
         __/ |       
        |___/        

   
   
   """
)
time.sleep(2)
