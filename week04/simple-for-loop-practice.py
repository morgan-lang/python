import time

userInput01 = input("Hi there. Please enter a word or phrase: ")

for item01 in userInput01:
    time.sleep(.2)
    print(item01)

time.sleep(1)
print("You entered ", "'", userInput01, "'")
input("Press the enter key to exit the program.")
