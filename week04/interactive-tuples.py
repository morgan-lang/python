while True:
    userInput01 = ((input("Enter an item to add to the inventory file. \n"
                      "Use as much description as you think is necessary: ")),
               (input("Enter the value of the item.\n"
                      "It isn't necessary to use a dollar sign: ")))
    print(userInput01[0])
    print(userInput01[1])
    continueinput = input("continue? y/n")
    if continueinput.lower() == "n":
        print("exiting")
        break