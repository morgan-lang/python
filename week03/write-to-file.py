import sys
import time


if(len(sys.argv) > 1):
    #The above is necessary to deal with cases where the user has input the path to the script but not any argument.
    #The reason it's greater than one is that the path itself counts as the first item in the array, therefore the
    # argument following the path is means the total number of items in the array is two, which is > 1.
    # Note that we're counting items in the array, not indicating their index number.

    #assigning user input to var userInput. Originally I tried to make this a global variable
    # by putting it right after import sys, but that resulted in an "out of range" error.
    userInput = sys.argv[1]

    if(userInput == "log"):
        print("Opening log file for editing")
        time.sleep(1)
        objFile = open("C:\\_Pythonclass\\log.txt", "a")
        objFile.write(input("Enter data to be appended to the log file:") + "\n")
        print("Writing to log file...")
        time.sleep(1)
        objFile.close()


    elif(userInput == "note"):
        print("Opening note file for editing")
        time.sleep(1)
        objFile = open("C:\\_Pythonclass\\note.txt", "a")
        objFile.write(input("Enter data to be appended to the note file:") + "\n")
        print("Writing to note file...")
        time.sleep(1)
        objFile.close()


    elif (userInput == "config"):
        print("Opening config file for editing")
        time.sleep(1)
        objFile = open("C:\\_Pythonclass\\config.txt", "a")
        objFile.write(input("Enter data to be appended to the config file:") + "\n")
        print("Writing to config file...")
        time.sleep(1)
        objFile.close()


    else:
        print("You must pass one of the following arguments to select a file to which to write data: log, note, or config.")

else:
    print("You must pass one of the following arguments to select a file to which to write: log, note, or config.")



