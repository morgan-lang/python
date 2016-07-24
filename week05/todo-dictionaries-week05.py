"""
Program name: todo-dictionaries-week05.py
Program function: to read a list of tasks and priorities from a text file into a dictionary,
then convert that dictionary into a list. Perform add, delete, and search operations on the items,
and provide an option to save the updated dictionary to the original text file.
Author: Morgan Lang
Date modified: 07/24/2016

"""

import csv
print("Welcome to the To-do List Doer.\n")
print("Current dictionary: \n")

# using csv.reader to open the file and parse tasks and priorities:
with open('todo.txt', mode='r') as fileInput01:
    readOperation = csv.reader(fileInput01)
    # formatting the dictionary:
    todoDictionary = {item[0]: item[1] for item in readOperation}
    print(todoDictionary, "\n")
    dictionaryCount = len(todoDictionary)
    print("There are", dictionaryCount, "tasks in this dictionary.")
    # Creating a list from the dictionary:
    oldItemList = list(todoDictionary.items())
    # Counting the list items:
    listCount = len(oldItemList)

# the main menu
while True:
    print(
        '''

        a - add items
        d - delete items
        s - search items
        w - write items to text file
        q - quit
        '''
    )

    mainUserInput = input("Enter a choice: ")

    # the exit condition:
    if mainUserInput == "q":
        break
    # check whether a key exists in the dictionary already; if not, add it:
    if mainUserInput == "a":
            print("adding items.\n")
            term = input("add a task: ")
            if term not in todoDictionary:
                definition = input("add a priority: ")
                todoDictionary[term] = definition
            print("Updated dictionary: ", todoDictionary)

    # search for a key:
    if mainUserInput == "s":
        term = input("Search for: ")
        if term in todoDictionary:
            definition = todoDictionary[term]
            print("Task found.", term, ":", definition)
        else:
            print(term, "not found")

    # delete a key/value pair:
    if mainUserInput == "d":
        print("Current tasks:\n")
        for item in todoDictionary:
            print(item)
        term = input("Which task would you like to delete? ")
        if term in todoDictionary:
            del todoDictionary[term]
            print("\n", term, "deleted.")
        else:
            print("\n", term, "not found.")

    # writing accumulated dictionary back to the file. This is the problematic part. Dictionaries are unordered, so my
    # attempt to export only a range of added values to avoid duplicates won't work. I should have performed this
    # export operation on a list rather than a dictionary. The formatting of the output is also wrong.
    # If I had time to do this assignment again, I would use a list in this section instead of a dictionary. Sorry!
    if mainUserInput == "w":
        newItemList = list(todoDictionary.items())
        print("List of items in current list: ", newItemList)
        listCount = len(newItemList)
        combinedCount = (int(dictionaryCount - 1) + int(listCount - 1))
        outputList = newItemList[dictionaryCount:combinedCount]
        print("There are", listCount, "items")
        fileWrite = open('todo.txt', 'a')
        for row in outputList:
            fileWrite.write(str(row) + "\n")
            print("The following data have been saved:\n")
            for item in outputList:
                print(item)
        fileWrite.close()