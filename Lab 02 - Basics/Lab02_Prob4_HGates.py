## Calculate the cost of aquarium and/or movie tickets

aquarium_only = float(input('How many aquarium only tickets were purchased? '))
movie_only = float(input('How many movie only tickets were purchased? '))
combo = float(input('How many combo tickets were purchased? '))

aquarium_only_cost = aquarium_only * 14
movie_only_cost = movie_only * 8
combo_cost = combo * ((14+8) * 0.75)
total_amount_due = aquarium_only_cost + movie_only_cost + combo_cost

print('Total Amount Due: $',format(total_amount_due, '.2f'))
