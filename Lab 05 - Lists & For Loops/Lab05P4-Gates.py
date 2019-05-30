#Lab 05 - Lists & For Loops Problem 3 - Range function and For loop
#Heather Gates

import random

# (a) Use for loop and random integer generator
# 5 integers in 1-9, Store in list, Display list
list1 = []
print('List 1:')
for i in range(5):
    num = random.randint(1,9)
    list1.append(num)
    #print(num)
print(list1)

#(b) Use for loop and random integer generator
# 5 integers in 2-8, store in list, display
list2 = []
print('List 2:')
for i in range(5):
    num2 = random.randint(2,8)
    list2.append(num2)
   # print(num2)
print(list2)

#(c) Use for loop to compare lists in pairs
print('Looped with while')
x = 0
while 0 <= x <= 4:
    if list1[x] > list2[x]:
        print('List 1:',list1[x], 'is larger')
    else:
        print('List 2:',list2[x], 'is larger')
    x = x + 1

print('Looped with for')
for index in range(0,5):
    if list1[index] > list2[index]:
        print('List 1:',list1[index], 'is larger')
    else:
        print('List 2:', list2[index], 'is larger')

print('Looped with for using max() function')
for index in range(0,5):
    maximum = max(list1[index], list2[index])
    print(maximum)
