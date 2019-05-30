# --------------------------------------------------------
# Lab 14 - Utility Bills
# Heather Gates

# This contains the electricity bill functions
# --------------------------------------------------------

from utility_bills import Utility_bill

class Electricity_bill(Utility_bill):

    def __init__(self, name, address, kwh=0, charge=0):
        base = super().__init__(name, address)
        self.__kwh = kwh
        self.__charge = charge

    def calculate_charge(self):

        self.__kwh = int(input('Please enter the number of kWh used: '))

        if self.__kwh <= 500:
            self.__charge = self.__kwh * 0.12
        else:
            self.__charge = 60 + ((self.__kwh - 500) * 0.15)

    def display_bill(self, name, address):

        print(name)
        print(address)
        print('kWh used: ', self.__kwh)
        print('Electricity Bill: $',self.__charge)
