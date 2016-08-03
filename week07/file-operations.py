from random import randint


text_file = open("file.txt", "r")
lines = text_file.readlines()
length = len(lines)
randomizer = randint(0, length)
print("The number of items in this list is:", length)
print("The items are as follows:", lines)
print("Here's a random line from the list:", lines[randomizer])
text_file.close()
input("enter/exit")