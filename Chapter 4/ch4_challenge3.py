# William Sumrall
# ITEC 1250
# Chapter 4, Challenge 3
# Improved Word Jumble

import random

# variable for counting failed guesses
fail = 0

# create a sequence of words to chose from
WORDS = ("horse", "monkey", "snake", "apple", "banana")

# pick one word randomly from the sequence
word = random.choice(WORDS)

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""

while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position + 1):]

# Start the game
print("\nWelcome to the Word Jumble Game!")
print("Unscramble the letters to make a word.")

print("\nThe jumble is:", jumble)

guess = input("\nYour guess: ")

while guess != correct and guess != "" and fail < 4 or guess == "hint":
    if guess != "hint":
        print("\nSORRY, THAT IS INCORRECT!", "Tip: write hint and get a hint.")
        fail = fail + 1
    guess = input("Your guess: ")
    if guess == "hint":
        print("Hint: ", correct[:(len(correct)-3)])
        continue

if guess == correct:
    print("\nTHAT IS CORRECT!")
    print("\nPoints: ", (5-(fail)))
elif fail <= 5:
    print("Points: 0")
    print("SORRY YOU FAIL!")

print("\nThanks for playing")

input("\nPress enter to exit game")
