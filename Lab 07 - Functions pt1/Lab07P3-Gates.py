# Lab 07 - Functions - Problem 3
# Heather Gates

def main():
    kwh = int(input('Please enter the number of kWh used: '))
    customer_type = input('Please enter customer type (R for residential or B for business: ')
    customer_type = customer_type.upper()
    while customer_type != 'R' and customer_type != 'B':
        print('ERROR: Please enter either R or B')
        customer_type = input('Please enter customer type (R for residential or B for business: ')
        customer_type = customer_type.upper()

    bill_calculator(k=kwh,ct=customer_type)


def bill_calculator(ct, k):
    if ct == 'R':
        if k <= 500:
            bill = k * 0.12
            print('Please pay this amount: $', format(bill,'.2f'))
        else:
            bill = 60 + (k - 500) * 0.15  # $60 is for the first 500 kWh
            print('Please pay this amount: $', format(bill, '.2f'))
    else:
        if k <= 800:
            bill = k * 0.16
            print('Please pay this amount: $', format(bill,'.2f'))
        else:
            bill = 128 + (k - 800) * 0.20  # $128 is for the first 800 kWh
            print('Please pay this amount: $', format(bill, '.2f'))

main()
