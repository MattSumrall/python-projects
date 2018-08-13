# William Sumrall
# ITEC 1250
# Chapter 3, Challenge 1
# Fortune Cookie Program

import random

print("Here is your fortune!")

randString = random.randint(1,5)

if randString == 1:
    print("\nYou will have a out of money experience.")

elif randString == 2:
    print("\nThis fortune is no good! Try another!")

elif randString == 3:
    print("\nStop eating now! Food poisoning no fun!")

elif randString == 4:
    print('\nWhen chosen for jury duty, tell judge fortune cookie say "guilty!"')

elif randString == 5:
    print("\nDrive like hell, you will get there.")

input("\nPress enter to exit.")

