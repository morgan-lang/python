import time
word = "steffi"

print("Enter the beginning and ending index numbers for the word 'steffi': ")
print("enter to exit")

start = None
#the below means 'while it is true that the entered value for start isn't empty
while start != "":
    start = (input("\nStarting index number in word 'steffi': "))

    if start:
        start = int(start)
        finish = int(input("Ending index number in word 'steffi': "))

        print(word, "for index range [",start,":",finish,"] is", end=" ")
        print(word[start:finish])
        time.sleep(.5)
        print("The complete index is ",word[:])
#and this is what we do if the entered value for start IS empty:
print("Exiting program after blank input received. Byyyye!")
time.sleep(1)