# this demonstrates the 'range' function. We increment the iteration because we start counting at 0, not 1.

print("let's count!\n")
for plotz in range(10):
    print(plotz + 1, end=" ")

print("\n\nCounting by threes: ")
for plotz in range(1, 27, 3):
    print(plotz + 1, end=" ")

print("\n\nCounting backwards: ")
for plotz in range(10, 0, -1):
    print(plotz, end=" ")

print("\n\nUsing each iteration in a range to trigger printing an arbitrary message: ")
for plotz in range(0, 10, 1):
    print("I like to repeat myself.")

input("\n\nenter to exit.")