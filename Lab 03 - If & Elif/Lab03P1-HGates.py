# Program to find the number of seconds since midnight when given Hours, Minutes, Seconds, and AM/PM

hour = int(input('Please enter the current hour: '))
minutes = int(input('Please enter the current minutes: '))
seconds = int(input('Please enter the current seconds: '))
meridian = input('Please enter the AM or PM: ')

meridian = meridian.upper() #to convert to upppercase
if hour == 12 and meridian == "AM": #midnight hour
    hour = 0
elif hour < 12 and meridian =='PM': #convert 12 hr to 24 hr for PM hours
    hour = hour + 12
else: hour = hour
since_midnight = (3600*hour) + (60*minutes) + seconds #calculate seconds
print('The time you entered is',hour, minutes, seconds, sep=":") # verificaiton that conditionals work
print('It has been',since_midnight, 'seconds since midnight.')
