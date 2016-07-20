# Loopy String

word = input("Enter a word, pal! ")

#Note that it's completely arbitrary what you call the letters in your word.
# I called them 'plotz' to underscore that. You're simply saying
# "go to the next logical unit within the variable 'word' and print each of those individual logical units, which
# happen to be letters (the smallest unit that can be dealt with), which I call plotz."
# Going through the sublevel of an element like a word is called 'iterating through a sequence.'
print("\nHere's each letter in your word: ")
for plotz in word:
    print(plotz)

input("\nPress enter to exit. ")