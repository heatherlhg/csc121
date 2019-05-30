# --------------------------------------------------------
# Lab 14 - Utility Bills
# Heather Gates

# This contains the main functions
# --------------------------------------------------------

from utility_bills import Utility_bill
from electricity_bill import Electricity_bill
from water_bill import Water_bill

def main():

    name = input('Please enter your name: ')
    address = input('Please enter your address: ')
    customer = Utility_bill(name, address)
    customer.name = name
    customer.address = address

    bill_choice = input('Which bill would you like to calculate? e for Electricity or w for Water ')
    bill_choice = bill_choice.lower()

    while bill_choice != 'e' and bill_choice != 'w':
        print('ERROR: please enter either e or w')
        bill_choice = input('Which bill would you like to calculate? e for Electricity or w for Water ')
        bill_choice = bill_choice.lower()

    if bill_choice == 'e':
        calc_elec = Electricity_bill(name, address)
        calc_elec.calculate_charge()
        calc_elec.display_bill(name,address,)
    else:
        calc_water = Water_bill(name, address)
        calc_water.calculate_charge()
        calc_water.display_bill(name, address)

main()
