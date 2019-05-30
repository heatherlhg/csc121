class Dinner_combo:

    def __init__(self, main_select, soup_select):

        self.__main_select = main_select
        self.__soup_select = soup_select
        self.__total = 0.0

    def choose_dish(self):

        self.__main_select = input('Please select your main dish: '
                                   'p for Sweet and Sour Pork, '
                                   'c for Sesame Chicken or '
                                   's for Shrimp Fried Rice '
                                   )
        self.__main_select = self.__main_select.lower()

        main_dish_opt = {'p': 'Sweet and Sour Pork',
                         'c': 'Sesame Chicken',
                         's': 'Shrimp Fried Rice'
                         }

        main_price_opt = {'p': 7.00,
                          'c': 8.00,
                          's': 9.00
                          }

        main_dish = main_dish_opt[self.__main_select]
        main_price = main_price_opt[self.__main_select]
        print('main dish', main_dish)
        print('main price', main_price)

    def choose_soup(self):

        self.__soup_select = input('Please select your soup: '
                                   'e for Egg Drop Soup or '
                                   'w for Wonton Soup '
                                   )
        self.__soup_select = self.__soup_select.lower()

        soup_opt = {'e': 'Egg Drop Soup',
                    'w': 'Wonton Soup'
                    }

        soup_price_opt = {'e': 1.25,
                          'w': 1.50
                          }

        soup = soup_opt[self.__soup_select]
        soup_price = soup_price_opt[self.__soup_select]
        print('soup', soup)
        print('soup price', soup_price)

    def display_order(self, main_dish, main_price, soup, soup_price):

        self.__total = main_price + soup_price
        print('You have ordered:', main_dish, 'and', soup)
        print('Your total is:', self.__total)
