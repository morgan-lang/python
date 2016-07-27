#   initialize the class
class MathClass(object):
    Number01 = None
    Number02 = None

    def AddValues(self):
        return float(self.Number01) + float(self.Number02)

    def SubtractValues(self):
        return float(self.Number01) - float(self.Number02)

    def MultValues(self):
        return float(self.Number01) * float(self.Number02)

    def DivValues(self):
        return float(self.Number01) / float(self.Number02)

objUserInput = MathClass()   # copy 1 of customer class. using it like a template
objUserInput.Number01 = input("Input number 1: ")
objUserInput.Number02 = input("Input number 2: ")
print(objUserInput.Number01, "plus ", objUserInput.Number02, "equals ", objUserInput.AddValues())
print(objUserInput.Number01, "minus ", objUserInput.Number02, "equals ", objUserInput.SubtractValues())
print(objUserInput.Number01, "multiplied by ", objUserInput.Number02, "equals ", objUserInput.MultValues())
print(objUserInput.Number01, "divided into ", objUserInput.Number02, "equals ", objUserInput.DivValues())
