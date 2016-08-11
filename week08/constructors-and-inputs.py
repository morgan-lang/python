#  How to get values into and out of classes and methods
# this class is used to create objects.

class Person(object):
    # this empty string is crucial.
    # note that the variable below is actually called a 'field' when it is used inside a class
    FirstName = ""
    LastName = ""

    def firstNameOutput(self):
        # this method is designed to display the first name field shown above
        return self.FirstName
        # this method is designed to display the last name field shown above
    def lastNameOutput(self):
        return self.LastName

    def __init__(self, FirstName, LastName):
        # Attributes
        self.FirstName = FirstName
        self.LastName = LastName

# initialization method. populating new objects with unique inputs using the init method from inside the class:
objP1 = Person(input("person 1 first name: "), input("person 1 last name: "))
# objP1.FirstName = "Bob"
# objP1.LastName = "Jones"

# and here's another object:
objP2 = Person(input("person 2 first name: "), input("person 2 last name: "))
# objP2.FirstName = "Sue"
# objP2.LastName = "Smith"

# and the outputs here string the names together:
print(objP1.firstNameOutput(), objP1.lastNameOutput())
print("-----------------------------")
print(objP2.firstNameOutput(), objP2.lastNameOutput())
input("enter to exit")