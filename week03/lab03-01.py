intVar = 2
if (intVar == 1):
    print("1")
#the reason why this nested if statement doesn't run
    # is that the above statement evaluates as "false," so the nested code won't get run.
    # Instead, the code goes directly to the else case
    if (intVar == 2):
        print("2")
else:
    print("other")