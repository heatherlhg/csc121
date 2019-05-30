# --------------------------------------------------------
# Lab 14 - Chinese Restaurant
# Heather Gates

# This contains the regular dinner combo functions
# --------------------------------------------------------

class Dinner_combo:

    def __init__(self, m_name='dish', s_name='soup', total=0):

        self.__main_dish = m_name
        self.__soup = s_name
        self.__total = total

    def choose_dish(self):

        self.__main_dish = input('Please select your main dish: '
                                 'p for Sweet and Sour Pork, '
                                 'c for Sesame Chicken or '
                                 's for Shrimp Fried Rice '
                                 )
        self.__main_dish = self.__main_dish.lower()

        while self.__main_dish != 'p' and self.__main_dish != 'c' and self.__main_dish != 's':
            print('ERROR: Please enter p, c, or s')
            self.__main_dish = input('Please select your main dish: '
                                     'p for Sweet and Sour Pork, '
                                     'c for Sesame Chicken or '
                                     's for Shrimp Fried Rice '
                                     )
            self.__main_dish = self.__main_dish.lower()

    def choose_soup(self):

        self.__soup = input('Please select your soup: '
                                   'e for Egg Drop Soup or '
                                   'w for Wonton Soup '
                                   )
        self.__soup = self.__soup.lower()

        while self.__soup != 'e' and self.__soup != 'w':
            print('ERROR: Please enter e or w')
            self.__soup = input('Please select your soup: '
                                'e for Egg Drop Soup or '
                                'w for Wonton Soup '
                                )
            self.__soup = self.__soup.lower()

    def display_order(self):

        if self.__main_dish == 'p':
            self.__main_dish = 'Sweet and Sour Pork'
            m_price = 7.00
        elif self.__main_dish == 'c':
            self.__main_dish = 'Sesame Chicken'
            m_price = 8.00
        elif self.__main_dish == 's':
            self.__main_dish = 'Shrimp Fried Rice'
            m_price = 9.00

        if self.__soup == 'e':
            self.__soup = 'Egg Drop Soup'
            s_price = 1.25
        elif self.__soup == 'w':
            self.__soup = 'Wonton Soup'
            s_price = 1.50

        self.__total = m_price + s_price

        print('Items ordered: ', self.__main_dish, ', ', self.__soup)
        print('Please pay this amount: $', format(self.__total, '.2f'))
