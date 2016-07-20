import time

tplRecord01 = (1, "Bob Smith", "bsmith@email.com")
tplRecord02 = (2, "Sue Jones", "suej@email.com")
tplRecord03 = (3, "Joe James", "jjames@email.com")
tplTable = (tplRecord01, tplRecord02, tplRecord03)

while(True):
    findCustomerName = input("Search for Customer Name: ")

    nameFound = False

    for row in tplTable:
        if(findCustomerName in row):
            print((findCustomerName) + " found. Customer ID: " + str(row[0]))
            nameFound = True

    if(nameFound == False):
        print("Customer name not found.")
    exitCase = input("Search for another name? (y/n): ")
    if(exitCase == "y"):
        continue
    else:
        print("Exiting program...")
        time.sleep(1)
        break