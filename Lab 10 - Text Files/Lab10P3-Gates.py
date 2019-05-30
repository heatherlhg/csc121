# Lab 10 - Working with Text Files - Problem 3
# Heather Gates

# Write a program to do the following.  Ask user to enter time in the format of hh:mm:ss. For example, 11:07:28.
# Hour must be a two-digit number between 0 and 23, inclusive.  Minute and second must be two-digit numbers between
# 0 and 59, inclusive.  The program needs to check whether the time entered is valid.
# (a)	Check whether there are exactly two colons. Display an error message and stop if the input is invalid.
# (b)	Check whether hour is a two-digit number. Display an error message and stop if the input is invalid.
# (c)	Check whether minute is a two-digit number. Display an error message and stop if the input is invalid.
# (d)	Check whether second is a two-digit number. Display an error message and stop if the input is invalid.
# (e)	Check whether hour is between 0 and 23, inclusive. Display an error message and stop if the input is invalid.
# (f)	Check whether minute is between 0 and 59, inclusive. Display an error message and stop if the input is invalid.
# (g)	Check whether second is between 0 and 59, inclusive. Display an error message and stop if the input is invalid.
# (h)	If the time entered is valid, remove the colons and display the time.  For example, if the input time is
# 11:07:28, the program should display 110728.

time = input('Please enter a time (HH:MM:SS): ')

if time.count(':') != 2:
    print('ERROR: Please use : to separate hours, minutes, and seconds.')
else:
    time_list = time.split(':')
    hour_split = time_list[0]
    minute_split = time_list[1]
    second_split = time_list[2]

    if not hour_split.isdigit() or len(hour_split) != 2:
        print('ERROR: Hours should be 2 digits e.g. 01')
    elif not minute_split.isdigit() or len(minute_split) != 2:
        print('ERROR: Minutes should be 2 digits e.g. 01')
    elif not second_split.isdigit() or len(second_split) != 2:
        print('ERROR: Seconds should be 2 digits e.g. 01')
    else:
        hour_split = int(hour_split)
        minute_split = int(minute_split)
        second_split = int(second_split)

        if hour_split < 0 or hour_split > 23:
            print('ERROR: hour is not within range (0-23).')
        elif minute_split < 0 or minute_split > 59:
            print('ERROR: minutes is not within range (0-59).')
        elif second_split < 0 or second_split > 59:
            print('ERROR: seconds is not within range (0-59).')
        else:
            numerical_time = str(hour_split) + str(minute_split) + str(second_split)
            print(numerical_time)
