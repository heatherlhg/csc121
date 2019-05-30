#Lab 05 - Lists & For Loops Problem 1 - Playing with integers
#Heather Gates

integers = []

#(a) ask user for input (b) display the list
another = 'y'
while another == 'y':
    new_integer = int(input('Please enter a number from 1 to 10: '))
    while new_integer < 1 or new_integer > 10:
        print('Error: You must enter a whole number between 1 and 10')
        new_integer = int(input('Please enter a number from 1 to 10: '))
    integers.append(new_integer)
    print('The numbers entered so far:', integers)
    another = input('Would you like to enter another number? [y,n] ')
    another = another.lower()
    while another != 'y' and another != 'n':
        print('Error: Please enter either y or n')
        another = input('Would you like to enter another number? [y,n] ')
        another = another.lower()

integers_length = len(integers)
print('There are', integers_length, 'numbers in the list.')

#(c) calculate and display average
total = 0
for digit in integers:
    total = total + digit
average = total/integers_length
print('The average of the numbers entered is:', format(average, '.1f'))

#(d) if average is over 7 subtract 1 from each number in the list
if average > 7:
    print('The average is over 7.')
    i = 0
    while i < integers_length:
        integers[i] = integers[i] - 1
        i = i + 1
    print('The new list of numbers is:', integers)
else:
    print('The average is not over 7.')
