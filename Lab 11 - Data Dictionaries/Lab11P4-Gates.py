# Lab 11 - Dictionaries, Sets & Exceptions - Problem 4
# Heather Gates

# Rewrite your program in Problem 3.  This time if what is entered by the user cannot be converted to an integer,
# display an error message and ask the user to reenter it until an integer is entered.

while True:
    try:
        number_of_hotdogs = int(input('How many hotdogs did you have? '))
        cost_of_hotdogs = float(number_of_hotdogs * 2.50)
        print('\n')
        break
    except ValueError:
        print('Invalid Input. Number of hotdogs must be a positive integer with no commas or decimals.')

while True:
    try:
        number_of_chips = int(input('How many packages of chips did you have? '))
        cost_of_chips = float(number_of_chips * 1.50)
        print('\n')
        break
    except ValueError:
        print('Invalid Input. Number of chips must be a positive integer with no commas or decimals.')

while True:
    try:
        number_of_sodas = int(input('How many sodas did you have? '))
        cost_of_sodas = float(number_of_sodas * 1.25)
        print('\n')
        break
    except ValueError:
        print('Invalid Input. Number of sodas must be a positive integer with no commas or decimals.')

total_amount_due = cost_of_hotdogs + cost_of_chips + cost_of_sodas

print('Total Amount Owed is $',format(total_amount_due,'.2f'))
