"""
Program name: todolist-revisited.py
Program function: create a class containing methods to read a list of tasks and priorities from a text file into a dictionary,
then convert that dictionary into a list. Perform add, delete, and search operations on the items,
and provide an option to save the updated dictionary to the original text file.
Author: Morgan Lang
Date modified: 07/28/2016

"""

import time

# initializing global variables:
textFile = "todo.txt"
readLine = ""
taskDictionary = {}


class todoRevisited(object):

    def readdisplay(self):
        print("Here are the current tasks and priorities in your to-do list:\n")
        # open the file and parse its contents:
        fileRead = open(textFile, "r")
        for line in fileRead:
            readLine = line  # reads a line of data
            fileList = readLine.split(",")    # this divides each line into 2 elements at the comma
            taskDictionary[fileList[0].strip()] = fileList[1].strip()   # defining keys and values for the dictionary.
            # the equals sign ties the key to its corresponding value.
            # we're pulling our dictionary pairs from the list fileList.
        fileRead.close()
        # formatting the dictionary for the user:
        for task, priority in taskDictionary.items():
            print(task + " (" + priority + ")")

    def inputloop(self):
        while True:
            print(
                '''

a - add items
d - delete items
f - find items
s - save items to text file and quit
q - quit without saving
                       '''

                  )
            # add a task and corresponding priority:
            mainMenuInput = (input("Select from the above options: "))
            if mainMenuInput == "a":
                userTask = (input("Enter a task: "))
                userPriority = (input("Enter a priority: "))
                taskDictionary[userTask] = userPriority
                print(taskDictionary)
                continue

            # delete a task and corresponding priority:
            elif mainMenuInput == "d":
                print("Here are the current tasks and priorities in your to-do list:\n")
                for task, priority in taskDictionary.items():
                    print(task)
                userRemove = input("Which task would you like to remove? ")
                if(userRemove in taskDictionary):
                    del taskDictionary[userRemove]
                else:
                    print("The task", userRemove, "was not found in the dictionary. "
                                                  "Please choose from the following tasks: \n")
                    for task, priority in taskDictionary.items():
                        print(task)
                continue

            # search for a task and display its corresponding priority:
            elif mainMenuInput == "f":
                userFind = input("Find task: ")
                if userFind in taskDictionary:
                    definition = taskDictionary[userFind]
                    print("Task found.", userFind, ":", definition)
                else:
                    print("The task", userFind, "was not found.\n")

            # format user input and save to the text file:
            elif mainMenuInput == "s":
                print("Saving file...")
                time.sleep(.5)
                fileRead = open(textFile, "w")
                for task, priority in taskDictionary.items():
                    fileRead.write(task + "," + priority + "\n")
                fileRead.close()
                break

            # the exit condition:
            elif mainMenuInput == "q":
                print("Exiting program...")
                time.sleep(.5)
                break

# creating a working copy of the todoRevisited class
todoRevisitedCopy = todoRevisited()

# calling the methods in order using the format class.method()
todoRevisitedCopy.readdisplay()
todoRevisitedCopy.inputloop()
