# Note: this is the same as week 4 lab 1. I changed the file name.

tplRecord01 = (1, "Bob Smith", "bsmith@email.com")
tplRecord02 = (2, "Sue Jones", "suej@email.com")
tplRecord03 = (3, "Joe James", "jjames@email.com")
divider = ("----------------------------------------")
tplTable = (tplRecord01, tplRecord02, tplRecord03)
tplHeader = ("ID#  ", "Name  ", "Email   ")

for thingy in tplHeader:
    print(str(thingy).strip("(").strip(")"))

for row in tplTable:
    #print(row)
    print(divider)
    for item in row:
        print(item)



input("\n\nenter to exit")