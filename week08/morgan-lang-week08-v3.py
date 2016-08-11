"""
Program name: morgan-lang-week08-v3.py
Program function: handle user input of product data, storing and retrieving product ID, description, and price
using a text file.
Notes: The code was originally just a set of functions. Our assignment was to reorganize the code using
at least one class. The two functions originally provided were subsumed as methods under a class called Productizer.
Then the I/O portion of the code was left out of the class and the methods were accessed using the class.method format.
Author: Morgan Lang
Date modified: 07/28/2016

"""


class Productizer:
    # Data
    objFile = None  # File Handle
    strUserInput = None  # A string which holds user input

    # Processing
    def WriteProductUserInput(File):
        try:
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while True:
                strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                if (strUserInput.lower() == "exit"):
                    break
                else:
                    File.write(strUserInput + "\n")
        except Exception as e:
            print("Error: " + str(e))

    def ReadAllFileData(File, Message="Contents of File"):
        try:
            print(Message)
            File.seek(0)
            print(File.read())
        except Exception as e:
            print("Error: " + str(e))


# I/O

try:
    Productizer.objFile = open("Products.txt", "r+")
    Productizer.ReadAllFileData(Productizer.objFile, "Here is the current data:")
    Productizer.WriteProductUserInput(Productizer.objFile)
    Productizer.ReadAllFileData(Productizer.objFile, "Here is this data was saved:")
except FileNotFoundError as e:
    print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
    if (Productizer.objFile != None):
        Productizer.objFile.close()
