import random
import time

word = input("type a word: ")

time.sleep(1)

print("The word you typed was", word, ".\n", "Now check this out. Cover the letter column with your hand and try to\n"
                                           "determine the letter based on index position. Remember that positive\n"
                                           "index numbers start at pos 0 and negative ones start at -1 and work\n"
                                           "backwards from the last item in the array (in this case, a letter.\n")

high = len(word)
low = -len(word)

time.sleep(1)

for i in range(10):
    position = random.randrange(low, high)
    print("word", "[", position, "]\t", word[position])

input("enter to exit")