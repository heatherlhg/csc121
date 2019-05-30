# --------------------------------------------------------
# Lab 14 - Utility Bills
# Heather Gates

# This contains the water bill functions
# --------------------------------------------------------

from utility_bills import Utility_bill

class Water_bill(Utility_bill):

    def __init__(self, name, address, gallons=0, charge=0):
        base = super().__init__(name, address)
        self.__gallons = gallons
        self.__charge = charge

    def calculate_charge(self):

        self.__gallons = int(input('Please enter the number of gallons used: '))

        if self.__gallons <= 6000:
            self.__charge = self.__gallons * 0.005
        else:
            self.__charge = 30 + ((self.__gallons - 6000) * 0.007)

    def display_bill(self, name, address):

        print(name)
        print(address)
        print('Gallons used:', self.__gallons)
        print('Water Bill: $', self.__charge)
