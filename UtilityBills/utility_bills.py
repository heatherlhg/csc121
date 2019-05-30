# --------------------------------------------------------
# Lab 14 - Utility Bills
# Heather Gates

# This contains the overall utility bill functions
# --------------------------------------------------------

class Utility_bill:

    def __init__(self, name, address, total=0):

        self.__name = name
        self.__address = address
        self.__total = total

    def calculate_charge(self):
        raise NotImplementedError('Method calculate_charge not implemented')

    def display_bill(self):
        raise NotImplementedError('Method display_bill not implemented')
