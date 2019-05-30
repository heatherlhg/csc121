# Lab 10 - Working with Text Files - Problem 1
# Heather Gates

# Write a program to store water usage data of 4 customers in a text file.  The program asks the user to enter account
# number, customer type (R for residential or B for business), and number of gallons used for each of the 4 customers.
# Store the data in a text file named “water.txt”.  Overwrite old data in “water.txt” if the file already exists.


def main():
    water_usage = open('water.txt','w')

    i = 4
    while i > 0:
        account_num = int(input('Please enter your account number: '))
        while len(str(account_num)) != 4:
            print('ERROR: Account number must be four numbers')
            account_num = int(input('Please enter your account number: '))
        customer_type = input('Please enter your account type (R for residential or B for business): ')
        customer_type = customer_type.upper()
        while customer_type != 'R' and customer_type != 'B':
            print('ERROR: Please enter either R for residential or B for business.')
            customer_type = input('Please enter your account type (R for residential or B for business): ')
            customer_type = customer_type.upper()
        gallons = int(input('Please enter the number of gallons used: '))
        while gallons < 0:
            print('ERROR: Usage cannot be negative.')
            gallons = int(input('Please enter the number of gallons used: '))
        water_usage.write(str(account_num))
        water_usage.write(' ')
        water_usage.write(customer_type)
        water_usage.write(' ')
        water_usage.write(str(gallons))
        water_usage.write('\n')
        i = i - 1

    water_usage.close()

main()

