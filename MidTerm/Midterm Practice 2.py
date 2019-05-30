# Midterm Practice 2
# Heather Gates

day = 0
temps = []
while day < 5:
    daily = int(input('Please enter a temperature: '))
    temps.append(daily)
    day = day + 1

print('Temperatures entered:', temps)
maximum = max(temps)
minimum = min(temps)
print('Highest temp:', maximum)
print('Lowest temp:', minimum)

sum = 0
for num in temps:
    sum = sum + num

average = sum / len(temps)
print('Average Temperature:', average)

sub = []
for x in temps:
    if x > average:
        sub.append(x)

print('The number of days hotter than average:', len(sub))
