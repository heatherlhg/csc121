## Calculate tip, tax, and total amount due from a restaurant bill

cost_of_food = float(input('How much was your food bill? '))

tax = cost_of_food * 0.07
tip = cost_of_food * 0.18
total_amount_due = cost_of_food + tax + tip

print('Food Bill: $',format(cost_of_food,'.2f'))
print('Sales Tax: $',format(tax,'.2f'))
print('Tip: $',format(tip,'.2f'))
print('Total Amount Due: $',format(total_amount_due,'.2f'))
