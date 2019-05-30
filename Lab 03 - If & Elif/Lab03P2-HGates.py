# program to convert seconds since midnight into hours, minutes, seconds, and AM/PM
since_midnight = int(input('Please input the number of seconds since midnight: '))

#math to find hr, min, sec
seconds = (since_midnight % 60)
minutes = (since_midnight % 3600)//60
hour = since_midnight //3600

# print(hour, minutes, seconds, sep=':') - this was to test that math was computed correctly

#add meridian and convet to 12 hour standard
if hour >= 12:
    meridian = 'PM'
    if hour > 12:
        hour = hour - 12
    print(hour, minutes, seconds, meridian, sep=':')
else:
    meridian = 'AM'
    if hour == 0:
        hour = hour + 12
    print(hour, minutes, seconds, meridian, sep=':')
