# --------------------------------------------------------
# Lab 12 - Modules - Problem 1
# Heather Gates

# We are writing a program to simulate a self-checkout system of a store named Wake-Mart.
#
# This program has four tasks at the top level: input prices of items, process discount, process promotion
# and process payment.  Processing of payment is further divided into two subtasks.  The customer can choose
# either to pay by cash or by debit card.

# --------------------------------------------------------


def main():

    """
    This function calls the scan_prices function to input item prices, calls the discount function to process
    discount, calls the promotion function to process gift card promotion, and call the make_payment
    function to process payment.
    """
    count, total = scan_prices()
    count, disc_total = discount(count, total)
    count, card_total = promotion(count, disc_total)
    make_payment(card_total)


def scan_prices():

    """
     This function gets the price of each item purchased.  The customer enters the prices one by one with a loop.
     When there are no more prices to enter, 0 is entered to exit the loop.  Whenever a negative price is entered,
     display “Price cannot be negative” and ask the user to enter next price.  Every time a valid price is entered,
     display the number of prices entered and the total so far (exclude invalid entries).  Return the number of
     prices entered and the total price of all items when the user has finished entering prices.
    """
    prices = []
    scan = 1
    total = 0

    while scan != 0:
        scan = float(input("Please enter a price or type '0' to exit. "))
        while scan < 0:
            print('ERROR: Price cannot be negative.')
            scan = float(input("Please enter a price or type '0' to exit. "))
        if scan != 0:
            prices.append(scan)
        total = total + scan
    count = len(prices)

    print('Total price of items entered: $', format(total, '.2f'))
    print('Total item count:', count)
    # print('List:', prices)
    print('')

    return count, total


def discount(count, total):

    """
    This function gives a 10% discount if 10 or more items are purchased.  It receives items count and
    total as arguments.  It checks whether 10 or more items are purchased, and reduces the total by 10% if
    the 10 or more items requirement is met.  This function returns the total, either it has been changed or not.
    """
    disc_total = total
    if count >= 10:
        disc_total = total * .90
        print("Congratulations! You've earned a discount! Your new total is:", format(disc_total, '.2f'))
    else:
        print('Must purchase 10 items to receive discount')

    print('')

    return count, disc_total


def promotion(count, disc_total):

    """
    This function allows the user to buy a gift card with discount.  It receives items count and total as arguments.
    If the total is $50 or higher, the user can choose to buy one $50 gift card for the price of $40.
    Update items count and total if the user chooses to buy gift card.  This function returns items count and total,
    either they have been changed or not.
    """
    card_total = disc_total
    if disc_total >= 50:
        card = input("SPECIAL OFFER: Do you want to buy a $50 gift card for $40? [Y/N]: ")
        card = card.upper()
        while card != 'Y' and card != 'N':
            print('ERROR: Please enter Y for yes or N for no.')
            card = input("SPECIAL OFFER: Do you want to buy a $50 gift card for $40? [Y/N]: ")
            card = card.upper()

        if card == 'Y':
            card_total = disc_total + 40
            count = count + 1
            print('Total with card: $', format(card_total, '.2f'))
            print('Item Count with card:', count)

    else:
        print('You did not spend $50 or more.')

    print('')

    return count, card_total


def make_payment(card_total):

    """
    This function allows the user to choose payment type [1 for cash, 2 for debit].  It receives balance as argument,
    and pass it to pay_cash and pay_debit.
    """
    payment = int(input('Please choose a payment type (1 for cash, 2 for debit): '))
    while payment != 1 and payment != 2:
        print("ERROR: Please enter 1 for cash or 2 for debit.")
        payment = input('Please choose a payment type (1 for cash, 2 for debit): ')

    if payment == 1:
        print('You have chosen to pay with cash.')
        pay_cash(card_total)
    else:
        print('You have chosen to pay with debit.')
        pay_debit(card_total)

    print('')

def pay_cash(card_total):

    """
    This function receives cash payment.  The self-checkout machine only accepts $10, $5 and $1 bills.
    Ask the user how many $10, $5 and $1 bills he is going to use.  Calculate and display total payment.
    If the total payment is lower than the balance, ask the user to reenter the numbers of $10, $5 and $1 bills
    until the total payment is not lower than the balance.  If customer has paid more than the balance,
    calculate and display change.
    """
    print('This machine can accept $10, $5, $1 bills.')

    cash = {'tens' : 0, 'fives' : 0, 'ones' : 0}
    balance = card_total
    while balance > 0:
        tens = int(input('Please enter the number of $10: '))
        while tens < 0:
            print("ERROR: Number cannot be negative.")
            tens = int(input('Please enter the number of $10: '))
        cash['tens'] = tens

        fives = int(input('Please enter the number of $5: '))
        while fives < 0:
            print("ERROR: Number cannot be negative.")
            fives = int(input('Please enter the number of $5: '))
        cash['fives'] = fives

        ones = int(input('Please enter the number of $1: '))
        while ones < 0:
            print("ERROR: Number cannot be negative.")
            ones = int(input('Please enter the number of $1: '))
        cash['ones'] = ones

        cash_in = (tens * 10) + (fives * 5) + (ones * 1)

        balance = card_total - cash_in

        print('You have paid: $', format(cash_in, '.2f'))
        if card_total > cash_in:
            print('You still owe: $', format(balance, '.2f'))
            print('Please inset more money.')
        elif cash_in > card_total:
            print('Your change is: $', format(abs(balance),'.2f'))
            print('Thank you for shopping with us.')
        else:
            print('Thank you for shopping with us.')

    print('')

    return card_total

def pay_debit(card_total):

    """
    This function receives debit payment.  It asks customer to enter a 16-digit card number and a 4-digit PIN.
    It also asks customer to enter payment amount.  Use a validation loop to ensure that payment is not lower
    than the balance.  If payment is lower than the balance, ask the user to reenter payment amount until it is
    not lower than the balance. If payment is higher than balance, calculate and display cash back amount.
    """

    balance = card_total
    print('Your total is: $', format(card_total, '.2f'))
    card_num = int(input('Please enter your 16 digit card number (no spaces or dashes): '))
    pin = int(input('Please enter your 4 digit PIN: '))
    card_pay = float(input('Please enter the payment amount: '))
    while card_pay < card_total:
        print('ERROR: Amount entered must be equal to or greater than the balance owed.')
        card_pay = float(input('Please enter the payment amount: '))
    balance = abs(card_total - card_pay)
    if card_pay > card_total:
        print('Your cash back is: $', format(balance, '.2f'))
    elif balance == 0:
        print('Thank you for shopping with us')

    print('')

    return card_total

main()
