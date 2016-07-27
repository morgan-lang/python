#   initialize the class
class Customer(object):
    Id = None
    Name = None

    def ToString(self):
        return str(self.Id) + ", " + str(self.Name)

objCustomer1 = Customer()   # copy 1 of customer class. using it like a template
objCustomer1.Id = 1
objCustomer1.Name = "Bob Smith"

objCustomer2 = Customer()   # copy 2 of customer class
objCustomer2.Id = 2
objCustomer2.Name = "Sue Jones"

print(objCustomer1.ToString())
print(objCustomer2.ToString())