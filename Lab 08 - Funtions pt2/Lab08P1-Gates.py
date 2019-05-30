# Lab 08 - Functions - Problem 1
# Heather Gates

# (a)	A main function: Call the value returning function get_kWh_used. Pass the return value to the value returning
# function bill_calculator as an argument. Display the return value of bill_calculator.


def main():
    kwh = get_kwh_used()
    bill_calculator(kwh)

# (b)	A get_kWh_used function: This function has no parameter.  It asks the user to enter number of kWh used.
# Use an input validation loop to ensure that kWh used is not negative. Return kWh used.


def get_kwh_used():
    kwh = int(input('Please enter the number of kWh used: '))
    while kwh < 0:
        print('ERROR: Please enter a positive number.')
        kwh = int(input('Please enter the number of kWh used: '))
    return kwh

 # (c)	A bill_calculator function: This function has a parameter to receive number of kWh used.
# Calculate and return the energy charge.


def bill_calculator(kwh):
    if kwh <= 500:
        bill = kwh * 0.12
        print('Please pay this amount: $', format(bill,'.2f'))
    else:
        bill = 60 + (kwh - 500) * 0.15  # $60 is for the first 500 kWh
        print('Please pay this amount: $', format(bill, '.2f'))


main()
