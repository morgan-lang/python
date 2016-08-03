try:
    num = float(input("enter a NUMBER, not a word. If you enter a word, an error will occur. Oh no."))
    print("You entered", num)
except:
    print("I don't think that's a number.")
input("enter/exit: ")