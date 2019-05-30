# Lab 11 - Dictionaries, Sets & Exceptions - Problem 3
# Heather Gates

#If the user enters anything that cannot be converted to an integer, display an error message and set the number
# of that item to 0.  For example, if the user enters 3.5 hotdogs, display “Invalid input. Number of hotdogs must
# be an integer” and set number of hotdogs to 0.  Do not ask the user to reenter number of hotdogs.

# Calculate amount owed from purchase of hotdogs, chips, and sodas

try:
    number_of_hotdogs = int(input('How many hotdogs did you have? '))
except ValueError:
    print('Invalid Input. Number of hotdogs must be an integer')
    number_of_hotdogs = 0

try:
    number_of_chips = int(input('How many packages of chips did you have? '))
except ValueError:
    print('Invalid Input. Number of chips must be an integer')
    number_of_chips = 0

try:
    number_of_sodas = int(input('How many sodas did you have? '))
except ValueError:
    print('Invalid Input. Number of sodas must be an integer')
    number_of_sodas = 0

cost_of_hotdogs = float(number_of_hotdogs * 2.50)
cost_of_chips = float(number_of_chips * 1.50)
cost_of_sodas = float(number_of_sodas * 1.25)

total_amount_due = cost_of_hotdogs + cost_of_chips + cost_of_sodas

print('Total Amount Owed is $',format(total_amount_due,'.2f'))
