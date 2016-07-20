import random

WORDS = ("asparagus", "plastron", "garbage", "polyamory", "asexual", "gleefully", "indomitable")

chosenWord = random.choice(WORDS)

correct = chosenWord

jumbleWord =""

while chosenWord:
    position = random.randrange(len(chosenWord))
    jumbleWord += chosenWord[position]
    chosenWord = chosenWord[:position] + chosenWord[(position +1):]

print(
    """
    Hi there. Welcome to Word Jumble.

        Unscramble the provided letters and guess the word.
        Press the enter key to quit.
    """
)

print("Your jumbled word is:\n\n", jumbleWord)

guess = input("\nPlease enter your guess: ")
while guess != correct and guess !="":
    print("Sorry, but that's wrong.")
    guess = input("Guess again: ")

if guess == correct:
    print("That's right. Great job.")

print("Thanks for playing and have a great day.")
input("Enter to exit.")
