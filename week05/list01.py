list01 = [input("add a thing."), input("add a thing."), input("add a thing."), "preexisting-list-thing4"]

print("there are", len(list01), "items in your inventory:")
for arbitrary in list01:
    print(arbitrary)
    askQuit = input("continue? y/n")
    if askQuit == "y":
        break



ask01 = input("which item do you want? Type a number between 0 and", len(list01), ".")

print("You chose item", ask01, ".", "That item is:", list01[ask01])
input("enter to exit")