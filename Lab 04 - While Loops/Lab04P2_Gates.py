#Lab 04 - While Loops Problem 2 - Seconds Since Midnight Error Check Loop
#Heather Gates

hour = int(input('Please enter the current hour: '))
while hour < 1 or hour > 12:
    print("Error: The hour entered must be between 1 and 12.")
    hour = int(input('Please enter the current hour: '))

minutes = int(input('Please enter the current minutes: '))
while minutes < 0 or minutes > 59:
    print("Error: The minutes entered must be between 0 and 59")
    minutes = int(input('Please enter the current minutes: '))

seconds = int(input('Please enter the current seconds: '))
while seconds < 0 or seconds > 59:
    print("Error: The seconds entered must be between 0 and 59")
    seconds = int(input('Please enter the current seconds: '))

meridian = input('Please enter the AM or PM: ')
meridian = meridian.upper() #to convert to upppercase
while meridian != 'AM' and meridian != 'PM':
    print("Error: Please enter either AM or PM")
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
