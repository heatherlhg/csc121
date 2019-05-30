# Lab 08 - Functions - Problem 2
# Heather Gates

# (a)	A main function: Call the value returning function get_user_input, which returns kWh used and customer type.
# Pass the return values to the value returning function bill_calculator as two arguments.
# Display the return value of bill_calculator.


def main():
    kwh, customer_type = get_user_input()
    bill_calculator(kwh,customer_type)


# (b)	A get_user_input function: This function has no parameter.  It asks the user to enter number of kWh used.
# Use an input validation loop to ensure that kWh used is not negative. Also ask the user to enter customer type
# (enter R for residential or B for business).  Convert lowercase letter to uppercase.
# Use an input validation loop to ensure that customer is either R or B. Return kWh used and customer type.


def get_user_input():
    kwh = int(input('Please enter the number of kWh used: '))
    while kwh < 0:
        print('ERROR: Please enter a positive number.')
        kwh = int(input('Please enter the number of kWh used: '))
    customer_type = input('Please enter customer type R for residential or B for business: ')
    customer_type = customer_type.upper()
    while customer_type != 'R' and customer_type != 'B':
        print('ERROR: Please enter either R or B')
        customer_type = input('Please enter customer type R for residential or B for business: ')
        customer_type = customer_type.upper()

    return kwh, customer_type

# (c)	A bill_calculator function: This function has two parameters to receive number of kWh used and customer type.
# Calculate and return the energy charge.


def bill_calculator(kwh, customer_type):
    if customer_type == 'R':
        if kwh <= 500:
            bill = kwh * 0.12
            print('Please pay this amount: $', format(bill,'.2f'))
        else:
            bill = 60 + (kwh - 500) * 0.15  # $60 is for the first 500 kWh
            print('Please pay this amount: $', format(bill, '.2f'))
    else:
        if kwh <= 800:
            bill = kwh * 0.16
            print('Please pay this amount: $', format(bill,'.2f'))
        else:
            bill = 128 + (kwh - 800) * 0.20  # $128 is for the first 800 kWh
            print('Please pay this amount: $', format(bill, '.2f'))


main()
