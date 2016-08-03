"""
Make a list. To save it to a text file, it must be converted to a string.
"""

Id = str(1)
Name = "Grace Jones"
lstRow1 = [Id, Name]
print(lstRow1.__str__())

# output to file
objFile = open("customers.txt", "a")
objFile.writelines(lstRow1[0] + "," + lstRow1[1] + "\n")
objFile.close()

objFile = open("customers.txt", "r")
for row in objFile:
    lstFileData = row.strip().split(",")
    print(lstFileData)

objFile.close()
print(lstFileData)

input("enter to exit")
