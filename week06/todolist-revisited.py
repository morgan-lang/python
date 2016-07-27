objFileName = "todo.txt"
strData = ""
dicTable = {}

# open the file and parse its contents:
objFile = open(objFileName, "r")
for line in objFile:
    strData = line  # reads a line of data
    lstData = strData.split(",")    # this divides each line into 2 elements at the comma
    dicTable[lstData[0].strip()] = lstData[1].strip()   # this defines the keys and values for the dictionary.
    # the equals sign ties key to value.
    # note that we're getting our dictionary pairs from a list, not the other way around!
objFile.close()

for strKey, strValue in dicTable.items():
    print(strKey + " (" + strValue + ")")

while True:
    print("1 for add, 2 for delete, 3 to save and quit")
    strChoice = str(input("enter choice: "))
    if (strChoice == "1"):
        strTask = str(input("enter task: "))
        strPriority = str(input("enter a priority: "))
        dicTable[strTask] = strPriority
        print(dicTable)
        continue

    elif(strChoice == "2"):
        for strKey, strValue in dicTable.items():
            print(strKey)
        strKeyToRemove = input("remove what?")
        if(strKeyToRemove in dicTable):
            del dicTable[strKeyToRemove]
        else:
            print("That ain't here, boss.")
        print(dicTable)
        continue

    elif(strChoice == "3"):
        objFile = open(objFileName, "w")
        for strKey, strValue in dicTable.items():
            objFile.write(strKey + "," + strValue + "\n")
        objFile.close()
        break
