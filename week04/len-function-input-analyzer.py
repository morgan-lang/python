#the len function determines length of strings & things

userInput = input("\nEnter some text: ")

print("\nThe length of your message, including spaces and punctuation (if any) is ", len(userInput))

print("\nThe most common letter in the English language, 'e,' ")

if "e" in userInput:
    print("is in your message.")

else:
    print("is not in your message.")

input("\nenter to exit.")
