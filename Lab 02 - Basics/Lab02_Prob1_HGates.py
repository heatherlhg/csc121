##Calculate amount owed from purchase of hotdogs, chips, and sodas

number_of_hotdogs = int(input('How many hotdogs did you have? '))
number_of_chips = int(input('How many packages of chips did you have? '))
number_of_sodas = int(input('How many sodas did you have? '))

cost_of_hotdogs = float(number_of_hotdogs * 2.50)
cost_of_chips = float(number_of_chips * 1.50)
cost_of_sodas = float(number_of_sodas * 1.25)

total_amount_due = cost_of_hotdogs + cost_of_chips + cost_of_sodas

print('Total Amount Owed is $',format(total_amount_due,'.2f'))
