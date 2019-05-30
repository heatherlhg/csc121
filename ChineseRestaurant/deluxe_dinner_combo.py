# --------------------------------------------------------
# Lab 14 - Chinese Restaurant
# Heather Gates

# This contains the deluxe dinner combo functions
# --------------------------------------------------------

from dinner_combo import Dinner_combo


class Deluxe_dinner_combo(Dinner_combo):

    def __init__(self, a_name='app', m_name='dish', s_name='soup', total=0):
        base = super().__init__(m_name, s_name, total)
        self.__appetizer = a_name

    def choose_appetizer(self):

        self.__appetizer = input('Please select your appetizer: '
                                 's for Spring Roll or '
                                 'c for Chicken Wing ')
        self.__appetizer = self.__appetizer.lower()

        while self.__appetizer != 's' and self.__appetizer != 's':
            print('ERROR: Please enter s or c')
            self.__appetizer = input('Please select your appetizer: '
                                     's for Spring Roll or '
                                     'c for Chicken Wing ')
            self.__appetizer = self.__appetizer.lower()

    def display_order(self):

        if self.__appetizer == 's':
            self.__appetizer = 'Spring Roll'
            a_price = 1.25
        elif self.__appetizer == 'c':
            self.__appetizer = 'Chicken Wing'
            a_price = 1.50
        self.__total = self.__total + a_price

        print('Items Ordered:', self.__appetizer)
        print('Please pay this amount: $', self.__total)
