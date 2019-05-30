# Lab 10 - Working with Text Files - Problem 2
# Heather Gates

# Write a program to read data stored in “water.txt”, which was created in Problem 1.
# Calculate water charge for each customer.
#
# Residential customers pay $0.005 per gallon for the first 6000 gallons.
# If the usage is more than 6000 gallons, the rate will be $0.007 per gallon after the first 6000 gallons.
#
# Business customers pay $0.006 per gallon for the first 8000 gallons.  If the usage is more than 8000 gallons,
# the rate will be $0.008 per gallon after the first 8000 gallons.
#
# Display account number and water charge of each customer on computer screen.


def main():
    water_usage = open('water.txt', 'r')
    for line in water_usage:
        account_num = line[0:4]
        customer_type = line[5]
        gallons = int(line[7:(len(line)-1)])
        if customer_type == 'R':
            if gallons <= 6000:
                bill = gallons * 0.005
            else:
                bill = 30 + (gallons - 6000) * 0.007  # 360 is for the first 6000 gallons
        else:
            if gallons <= 8000:
                bill = gallons * 0.006
            else:
                bill = 48 + (gallons - 8000) * 0.008  # $48 is for the first 8000 gallons
        print('Account Number:', account_num, ' Water Charge: $', format(bill, '.2f'))
    water_usage.close()

main()
