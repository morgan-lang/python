import time

header01 = ["ID", "Name", "        Email",]
record01 = [1, "Bob Smith", "bsmith@bsmith.com"]
record02 = [2, "Sue Jones", "sjones@sjones.com"]
record03 = [3, "Joe Jones", "jjones@jjones.com"]
table01 = [header01, record01, record02, record03]

number = int(len(table01))
print("There are ", number - 1, " records in the table.")
for item in table01:
    print(item)

while True:
    intID = int(input("ID: "))
    strName = input("Name: ")
    strEmail = input("Email: ")
    userRow = [intID, strName, strEmail]
    table01.append(userRow)
    for item in table01:
        print(item)
    if(input("add another record? y/n: ")).lower() == "y":
        continue
    else:
        break

userSave = input("Save to file? y/n: ")
if(userSave.lower() == "y"):
    fileWrite = open('lab05-1-table-as-list.txt', 'a')
    for row in table01:
        fileWrite.write(str(row).replace("[", "").replace("]", "").replace("'", "") + "\n")
    fileWrite.close()
    print("The following data have been saved:\n")
    for item in table01:
        print(item)
    input("Enter to exit: ")


else:
    input("Data not saved. Enter to exit.")