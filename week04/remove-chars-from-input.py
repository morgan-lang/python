import time
message = input("Enter a message: ")

replacementMessage = ""

VOWELS = "aeiou"

print()
#interesting use of print to show the iteration procedure and looping
for item in message:
    time.sleep(.2)
    if item.lower() not in VOWELS:
        #below is the increment procedure. item = letters in the message and += means increment to next match
        replacementMessage += item
        print("iterating and removing vowel\n", replacementMessage)

print("\nYour message without vowels is: ", replacementMessage)

input("enter to exit")