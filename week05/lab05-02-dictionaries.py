import time

record01 = {"ID": "1", "Name": "Bob Smith", "Email": "bsmith@bsmith.com"}
record02 = {"ID": "2", "Name": "Sue Jones", "Email": "sjones@sjones.com"}
record03 = {"ID": "3", "Name": "Joe Jones", "Email": "jjones@jjones.com"}
table01 = [record01, record02, record03]

number = int(len(table01))
print("There are ", number, " records in the table.")
for item in table01:
    print(item)

while True:
    intID = int(input("ID: "))
    strName = input("Name: ")
    strEmail = input("Email: ")
    userRow = {"ID": intID, "Name": strName, "Email": strEmail}
    table01.append(userRow)
    for item in table01:
        print(item)
    if(input("add another record? y/n: ")).lower() == "y":
        continue
    else:
        break

userSave = input("Save to file? y/n: ")
if userSave.lower() == "y":
    fileWrite = open('lab05-2-dictionaries.txt', 'a')
    for row in table01:
        fileWrite.write(str(row) + "\n")
    fileWrite.close()
    print("The following data have been saved:\n")
    for item in table01:
        print(item)
    input("Enter to exit: ")


else:
    input("Data not saved. Enter to exit.")