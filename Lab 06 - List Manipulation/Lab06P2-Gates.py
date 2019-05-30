#Lab 06 - List Manipulation Problem 2 - Working with Tuples and Concatenation
#Heather Gates

import random

# Generate 10 random numbers between 1 & 15 and store in a tuple. Display tuple
list1 = []
print('Tuple of 10 Random Numbers:')
for i in range(10):
    num = random.randint(1,15)
    list1.append(num)
    #print(num)
tuple1 = tuple(list1)
print(tuple1)

# Create new tuple. Copy first 3 elements from first tuple. Display tuple.
tuple2 = tuple1[0:3]
print('Tuple of First 3 Numbers')
print(tuple2)

# Create new tuple. Copy last 3 elements from first tuple. Display tuple.
tuple3 = tuple1[7:10]
print('Tuple of Last 3 Numbers')
print(tuple3)

# Concatenate tuple2 and tuple3. Display
tuple4 = tuple2 + tuple3
print('Two Tuples Concatenated')
print(tuple4)

# Sort Tuple & display
print('Two Tuples Concatenated and Sorted')
list2 = list(tuple4)
list2.sort()
tuple4 = tuple(list2)
print(tuple4)

