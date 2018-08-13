# William Sumrall
# ITEC 1250
# Chapter 3, Challenge 2
# Coin Flip Program

import random

num = 100

flips = [random.randint(0,1) for r in range(num)]

results = []

for object in flips:
    if object == 0:
        results.append("Heads")
        
    elif object == 1:
        results.append("Tails")

print(results)

input("\nPress enter to exit.")
        
