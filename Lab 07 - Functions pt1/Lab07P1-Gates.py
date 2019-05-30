# Lab 07 - Functions - Problem 1
# Heather Gates

def main():
    kwh = int(input('Please enter the number of kWh used: '))

    bill_calculator(kwh)


def bill_calculator(kwh):
    if kwh <= 500:
        bill = kwh * 0.12
        print('Please pay this amount: $', format(bill,'.2f'))
    else:
        bill = 60 + (kwh - 500) * 0.15  # $60 is for the first 500 kWh
        print('Please pay this amount: $', format(bill, '.2f'))


main()
