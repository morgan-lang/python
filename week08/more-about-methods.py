#  How to get values into and out of classes and methods
# this class is used to create objects.

class Person(object):
    # this empty string is crucial.
    # note that the variable below is actually called a 'field' when it is used inside a class
    # we're commenting these out because using fields is redundant when using attributes
    # Fields:
    # FirstName = ""
    # LastName = ""


    # Constructor:
    def __init__(self, FirstName = "DefaultFirstname", LastName = "DefaultLastname"):  # default values
        # Attributes, used instead of setting fields at the top:
        self.__FirstName = FirstName  # the underscores make it 'private'
        self.__LastName = LastName  # the underscores make it 'private'

    # Properties:
    # These are processing actions we can perform on attributes. We can't do processing in a constructor.
    # FirstName:
    @property  # the getter or accessor property flag
    def FirstName(self):
        return self.FirstName()

    @property  # the getter or accessor property flag
    def LastName(self):
        return self.LastName()

    @FirstName.setter  # the setter property flag
    def FirstName(self, Value):
        if Value is not None:  # checking for empty strings, but you could do fancier logic here.
            self.__FirstName = Value

    @LastName.setter  # the setter property flag
    def LastName(self, Value):
        if Value is not None:  # checking for empty strings, but you could do fancier logic here.
            self.__LastName = Value

    # Methods:
    # These work with the constructor, not fields:
    def firstNameOutput(self):
        return self.__FirstName.lower()

    def lastNameOutput(self):
        return self.__LastName.lower()

# initialization method that doesn't rely on fields. Note that we're overriding default values.
# Note that we CAN set these values for 'private' attributes because we are interacting with the constructor and not
# setting values directly:
objP1 = Person("Bob", "Jones")
# objP1.FirstName = "Bob"
# objP1.LastName = "Jones"

# and here's another object, this time using the default values set in the constructor:
objP2 = Person("Sue", "Smith")
# now here's something that WON'T work. We're trying to set real values of attributes directly without going through
# the constructor , as we did with the Bob Jones example above. When we run this code, we'll get blank output rather
# than an error.
objP2.__FirstName = "Sue"
objP2.__LastName = "Smith"

# and the outputs here string the names together:
print(objP1.firstNameOutput(), objP1.lastNameOutput())
print("-----------------------------")
print(objP2.firstNameOutput(), objP2.lastNameOutput())
print(objP2)
input("enter to exit")

# Inheriting the Person class and redefining it as the employee class:

class Employee(Person):
    None

objE1 = Employee("Joe", "Bloggs")

print(objE1.firstNameOutput(), objE1.lastNameOutput())
