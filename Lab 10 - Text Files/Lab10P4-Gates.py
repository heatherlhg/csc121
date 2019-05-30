# Lab 10 - Working with Text Files - Problem 4
# Heather Gates

# Write a program to do the following.
# Ask the user to enter a string.
# Convert all letters to uppercase.
# Count and display the frequency of each letter in the string.
# Each letter cannot be shown more than once in the output.
# The program should count letters only but no other characters.

string = input('Please type a sequence of characters (letters, numbers, special characters): ')
string = string.upper()

for letter in string:
    if letter.isalpha():
        s = string.count(letter)
        print(letter, s)
