# v1 = None
# v2 = None
# lstData = None

def addValues(value1, value2):
    decAnswer = value1 + value2
    lstResults = [decAnswer, value1, value2]
    return lstResults

def subValues(value1, value2):
    decAnswer = value1 - value2
    lstResults = [decAnswer, value1, value2]
    return lstResults

def multValues(value1, value2):
    decAnswer = value1 * value2
    lstResults = [decAnswer, value1, value2]
    return lstResults

def divValues(value1, value2):
    decAnswer = value1 / value2
    lstResults = [decAnswer, value1, value2]
    return lstResults

v1 = float(input("enter a number: "))
v2 = float(input("enter another number: "))
lstData = addValues(v1, v2)
print("The sum of the values " + str(lstData[1]) + " and " + str(lstData[2]) + " is " + str(lstData[0]))

lstDatadiv = subValues(v1, v2)
print("The diff of the values " + str(lstDatadiv[1]) + " and " + str(lstDatadiv[2]) + " is " + str(lstDatadiv[0]))

lstDatamult = multValues(v1, v2)
print("The product of the values " + str(lstDatamult[1]) + " and " + str(lstDatamult[2]) + " is " + str(lstDatamult[0]))

lstDatadiv = divValues(v1, v2)
print("The quotient of the values " + str(lstDatadiv[1]) + " and " + str(lstDatadiv[2]) + " is " + str(lstDatadiv[0]))


