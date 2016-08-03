# file must exist first

# data
objFile = None
strUserInput = None
strUserInput2 = None

# processing
def writeProductUserInput(theFile):
    print("Hello and welcome to the Productizer. \n"
          "Type 'exit' to exit the program.")
    while True:
        strUserInput = input("Enter a thing: ")
        strUserInput2 = input("Enter another thing: ")
        if (strUserInput.lower() == "exit"):
            break
        elif (strUserInput2.lower()) == "exit":
            break
        else:
            theFile.write(strUserInput + strUserInput2 + "\n")

def ReadAllFileData(theFile, Message="Contents of File"):
    print(Message)
    theFile.seek(0)
    print(theFile.read())

# I/O
try:
    objFile = open("products.txt", "r+")  # see page 193
    ReadAllFileData(objFile, "here are the current data: ")
    writeProductUserInput(objFile)
    ReadAllFileData(objFile, "The following data were saved: ")
except Exception as e:
    print("Oh, dear. I'm terribly sorry, but the following error occurred: \n", e.__str__())
finally:
    if objFile is not None:
        objFile.close()
    print("the program has closed.")
input("enter to exit")