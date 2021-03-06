# CSC 121.0003 Midterm Programming Exam
# Program 1 Rental Car Fees
# Heather Gates

car_type = input('Please choose compact, mid-size, or full size car type: [C, M, F] ')
car_type = car_type.upper()

if car_type != 'C' and car_type != 'M' and car_type != 'F':
    print('Invalid car type. Program Ended')
else:
    days = int(input('Please enter the number of days rented: '))
    if days <= 0:
        print('Invalid number of days. Program Ended.')
    else:
        car_size = ['C','M','F']
        rate = [30, 37 ,45]
        disc_rate = [26, 32, 38]
        for x in range(3):
            if car_type == car_size[x]:
                print(rate_option)
        if days <=3:
            fee = rate[rate_option] * days
        else:
            fee = rate[rate_option] * 3 + (days - 3) * disc_rate[rate_option]

        print('You are renting the car for', days, 'days.')
        print('Your rate is', rate[rate_option], 'for the first 3 days and', disc_rate[rate_option], 'for all remaining days.')
        print("The total rental fee is: ", fee)


# CSC 121.0003 Midterm Programming Exam
# Program 1 Rental Car Fees
# Heather Gates

car_type = input('Please choose compact, mid-size, or full size car type: [C, M, F] ')
car_type = car_type.upper()

if car_type != 'C' and car_type != 'M' and car_type != 'F':
    print('Invalid car type. Program Ended')
else:
    days = int(input('Please enter the number of days rented: '))
    if days <= 0:
        print('Invalid number of days. Program Ended.')
    else:
        rate = [30, 37 ,45]
        disc_rate = [26, 32, 38]
        if car_type == 'C':
            rate_option = 0
            type_name = 'Compact'
        elif car_type == 'M':
            rate_option = 1
            type_name = 'Mid-size'
        else:
            rate_option = 2
            type_name = 'Full-size'

        if days <=3:
            fee = rate[rate_option] * days
        else:
            fee = rate[rate_option] * 3 + (days - 3) * disc_rate[rate_option]

        print('Your chosen car size is:', type_name)
        print('You are renting the car for', days, 'days.')
        print('Your rate is $', rate[rate_option], 'for the first 3 days and $', disc_rate[rate_option], 'for all remaining days.')
        print("The total rental fee is: $", fee)
