# Craps Roller
# Demonstrates Random Number Generation

import random # must import for random method to work

# generate random from 1-6
die1 = random.randint(1,6)
die2 = random.randrange(6) + 1

total = die1 + die2

print("You rolled a", die1, "and a", die2, "for a total of", total)

input("\n\nPress ENTER to exit the program.")