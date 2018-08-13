# William Sumrall
# ITEC 1250
# Chapter 4, Challenge 1
# Count My Number Program

number = 0

print("Welcome to the counting program!")

start = int(input("\nEnter the number you want to start counting from: "))
stop = int(input("\nEnter the count ending number: "))
amount = int(input("\nEnter the amount by which to count: "))

for number in range(start, stop + 1, amount):
    print(number)

input("\nPress enter to exit program.")

