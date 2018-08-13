# William Sumrall
# ITEC 1250
# Chapter 4, Challenge 1
# Reverse Message Program

print("\nWelcome to the Reverse Message Program")

message = input("\nEnter in your message here: ")

print("\nThis is your message reversed.")

message_length = len(message)

message_reversed = message[-1:-(message_length +1):-1]

print(message_reversed)

input("\nPress enter to exit.")


