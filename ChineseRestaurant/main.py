# --------------------------------------------------------
# Lab 14 - Chinese Restaurant
# Heather Gates

# This contains the main function
# --------------------------------------------------------

from dinner_combo import Dinner_combo
from deluxe_dinner_combo import Deluxe_dinner_combo


def main():

    combo_select = input('Please select your combo type: '
                         'r for regular (main dish and soup or) '
                         'd for deluxe (main dish, soup, and appetizer) '
                         )
    combo_select = combo_select.lower()

    while combo_select != 'r' and combo_select != 'd':
        print('ERROR: Please select r or d.')
        combo_select = input('Please select your combo type: '
                             'r for regular (main dish and soup or) '
                             'd for deluxe (main dish, soup, and appetizer) '
                             )
        combo_select = combo_select.lower()

    if combo_select == 'r':
        order_summary = Dinner_combo()
        order_summary.choose_dish()
        order_summary.choose_soup()
        order_summary.display_order()

    else:
        order_summary = Deluxe_dinner_combo()
        order_summary.choose_dish()
        order_summary.choose_soup()
        order_summary.choose_appetizer()
        order_summary.display_order()

main()
