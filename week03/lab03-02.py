# 1)	Write a script that lets a user select one of three options by entering an argument when the script starts.
# 2)	Start by typing these comments out and use them as pseudo code.
# Get the argument value
import sys

# Execute if 1, 2, or 3 is selected
if(len(sys.argv) > 1):
    #The above is necessary to deal with cases where the user has input the path to the script but not any argument.
    #The reason it's greater than one is that the path itself counts as the first item in the array, therefore the
    # argument following the path is means the total number of items in the array is two, which is > 1.
    # Note that we're counting items in the array, not indicating their index number.
    #
    # 3)	Now add if, elif, and else statements to your script so that it prints out an appropriate message based on
    # the number passed to the script when it executes.

    #assigning user input to var userInput. Originally I tried to make this a global variable
    # by putting it right after import sys, but that resulted in an "out of range" error.
    userInput = sys.argv[1]
# Print "You chose one" only if option 1 is selected.
    if(userInput == "1"):
        print("You chose one")

# Print "You chose two" execute only if option 2 is selected.
    elif(userInput == "2"):
        print("You chose two")

# Print "You chose three" execute only if option 3 is selected.
    elif (userInput == "3"):
        print("You chose three")

# Print "Please choose 1, 2, or 3"

    else:
        print("You must pass one of the following arguments: 1, 2, or 3.")

else:
    print("You must pass one of the following arguments: 1, 2, or 3.")



