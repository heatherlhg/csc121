# Lab 07 - Functions - Problem 2
# Heather Gates

def main():
    kwh = int(input('Please enter the number of kWh used: '))
    customer_type = input('Please enter customer type (R for residential or B for business: ')
    customer_type = customer_type.upper()
    while customer_type != 'R' and customer_type != 'B':
        print('ERROR: Please enter either R or B')
        customer_type = input('Please enter customer type (R for residential or B for business: ')
        customer_type = customer_type.upper()

    bill_calculator(kwh,customer_type)


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

