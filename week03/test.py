#Program function: to create an inventory file, display its contents, and allow user input to be added to it.
#Author: Morgan Lang
#Date modified: 07/07/2016
#################################################################

import time

# Splash / welcome. Yes, it's goofy. I don't care.
print(
    '''
  ___                 _                    _      _    _              ___
 |_ _|_ ___ _____ _ _| |_ ___ _ _ _  _    /_\  __| |__| |___ _ _ ___ / _ \ _ _  _ _  ___ _ _
  | || ' \ V / -_) ' \  _/ _ \ '_| || |  / _ \/ _` / _` / -_) '_|___| (_) | ' \| ' \/ -_) '_|
 |___|_||_\_/\___|_||_\__\___/_|  \_, | /_/ \_\__,_\__,_\___|_|      \___/|_||_|_||_\___|_|
                                  |__/

    '''
)

#First we'll need to create our inventory file if it doesn't exist. We'll do that by opening it in append mode.
#If it doesn't exist, it will be created. There's probably a better way to do this.
inventoryFileCreate = open("C:\\_Pythonclass\\HomeInventory.txt", "a")
inventoryFileCreate.close()

# Now we'll display the current contents of the inventory by opening the target file in 'read' mode:
inventoryFileRead = open("C:\\_Pythonclass\\HomeInventory.txt", "r")
print("Current inventory: \n", inventoryFileRead.read())
# Closing the file so that inventoryFile can open it below
inventoryFileRead.close()

# Now we'll open our inventory file in 'append mode'
inventoryFileWrite = open("C:\\_Pythonclass\\HomeInventory.txt", "a")

# Giving the user some context and basic information.
print("Welcome to the Inventory Adder-Onner.\n"
      "This program adds inventory items to the following file: C:\\_Pythonclass\\HomeInventory.txt\n\n")

# Pausing for dramatic effect
time.sleep(1)

# We want to use a while loop because we need to keep prompting for input until the user chooses to quit.
while True:
    # Prompting for an item description
    userInput01 =(input("Enter an item to add to the inventory file. \n"
                        "Use as much description as you think is necessary: "))

    # Prompting for an item value
    userInput02 =(input("Enter the value of the item.\n "
                        "It isn't necessary to use a dollar sign: "))

    # Now we want to format the output of what will be written to the file.
    # Adding spaces, a dash, and the dollar sign helps readability.
    combinedInput = userInput01 + " " + "-" + " " + "$" + userInput02

    #Write the formatted output and add a new line for the next item.
    inventoryFileWrite.write(combinedInput + "\n")

    #It's always good to provide feedback and context so the user can understand what's happening.
    print("This item will be added to the inventory upon exiting the program. \n")

    # Providing the user with a way to exit or continue the program
    userInput03 =(input("Press the 'enter' or 'return' key to continue adding items."
                        "\n Type 'exit' to quit this program and add the new inventory items. \n"))

    # The exit condition. We'll convert userInput03 to lowercase to be sure we catch 'Exit' and 'EXIT'
    if userInput03.lower() == "exit":
        print("Adding items to file and preparing to exit...")
        time.sleep(.5)
        print("Thanks for using the Inventory Adder-Onner. See you next time!")
        time.sleep(2)
        break
# Closing the inventory file.
inventoryFileWrite.close()
