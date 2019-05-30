# Lab 11 - Dictionaries, Sets & Exceptions - Problem 1
# Heather Gates

# (a)	Ask the user to enter a string.  Convert all letters to uppercase.  Count the frequency of each letter in the
# string. Store the frequency counts in a dictionary.  You should count letters only.  Do not count any other characters
#  such as digits and space.  Display the dictionary.

string = input('Please enter a word or phrase: ')
string = string.upper()

letter_count = {}

for letter in string:
    if letter.isalpha():
        s = string.count(letter)
        letter_count[letter] = s
        #print(letter, s) # for verification purposes

print('Initial Dictionary:', letter_count)

# (b)	Ask the user to enter a letter.  Convert it to uppercase.  Check whether the letter is in the dictionary.
# If it is not, display the message “Letter not in dictionary”.  Otherwise, display the frequency count of that letter,
# remove the letter from the dictionary and display the dictionary after that letter has been removed.

new_letter = input('Please enter a single letter: ')
new_letter = new_letter.upper()

if new_letter not in letter_count:
    print('Letter not in dictionary.')
else:
    print(new_letter, 'appears', letter_count[new_letter], 'times.')
    del letter_count[new_letter]
    print('Dictionary after letter removed:', letter_count)

# (c) Create a list to store the letters that are in the dictionary.  Sort and display the list.

dict_list = list(letter_count.keys())
dict_list.sort()
print('Letters sorted:', dict_list)
