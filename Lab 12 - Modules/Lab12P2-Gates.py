# --------------------------------------------------------
# Lab 12 - Modules Problem 2
# Heather Gates

# Define a main function in the main module to do the following:
# (1)	Ask the user to choose a foreign currency: Euro, Japanese Yen or Mexican Peso.
#       Write a loop to validate user input. If an invalid choice is made, display an error message and ask the user to
#       choose a foreign currency again until the choice is valid.
# (2)	Ask the user to enter US dollar amount. Write a loop to validate user input. If the US dollar amount is
#       negative, display an error message and ask the user to reenter it until it is non-negative.
# (3)	Call one of the three functions in the currency module to convert US dollar to the foreign currency
#       chosen by the user
# (4)	Receive and display the converted foreign currency
# --------------------------------------------------------

import currency


def main():
    currency_choice = input('Please choose a currency [e for Euro, y for Yen, or p for Peso]: ')
    currency_choice = currency_choice.upper()
    while currency_choice != 'E'  and currency_choice != 'Y' and currency_choice != 'P':
        print('ERROR: Please enter e for Euro, y for Yen, or p for Peso.')
        currency_choice = input('Please choose a currency [e for Euro, y for Yen, or p for Peso]: ')
        currency_choice = currency_choice.upper()

    dollar = float(input('Please enter the amount of dollars (USD) to convert: '))
    while dollar < 0:
        print('ERROR: Amount cannot be negative.')
        dollar = float(input('Please enter the amount of dollars (USD) to convert: '))

    if currency_choice == 'E':
        euro = currency.to_euro(dollar)
        print(format(dollar, '.2f'), "USD is", format(euro, '.2f'), 'EUR')
    elif currency_choice == 'Y':
        yen = currency.to_yen(dollar)
        print(format(dollar, '.2f'), 'USD is', format(yen, '.2f'), 'JPY')
    elif currency_choice == 'P':
        peso = currency.to_peso(dollar)
        print(format(dollar, '.2f'), 'USD is', format(peso, '.2f'), 'MXN')
    else:
        print('No conversion occurred.')


main()
