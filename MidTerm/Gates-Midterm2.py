# CSC 121.0003 Midterm Programming Exam
# Program 2
# Heather Gates

# (a) [2 points] Generate 6 random integers from 10 to 20, inclusive. Store the random integers in a list.
# Name it list1. Display list1.

import random

list1 = []
print('List 1:')
for i in range(6):
    num = random.randint(10,20)
    list1.append(num)
print(list1)

# (b) [2 points] Generate 6 random integers from 15 to 25, inclusive. Store the random integers in a list.
# Name it list2. Display list2.

list2 = []
print('List 2:')
for i in range(6):
    num = random.randint(15,25)
    list2.append(num)
print(list2)

# (c) [2 points] Concatenate the first 3 elements of list1 and the last 3 elements of list2 to form a new list.
# Name it list3. Display list3.

list3 = list1[0:3] + list2[0:3]
print('List 3: ')
print(list3)

# (d) [2 points] Concatenate the last 3 elements of list1 and the first 3 elements of list2 to form a new list.
# Name it list4. Display list4.

list4 = list1[3:6] + list2[3:6]
print('List 4: ')
print(list4)

# (e) [2 points] Sort elements of list3 in ascending order (i.e. from small to large). Display the sorted list3.

list3.sort()
print('List 3 sorted:')
print(list3)

# (f) [2 points] Sort elements of list4 in descending order (i.e. from large to small). Display the sorted list4.

list4.sort()
list4.reverse()
print('List 4 reverse sorted:')
print(list4)

# (g) [2 points] Create a list to store list3 and list4.  Name it big_list.  This is a list of lists.
# The first element of big_list is list3. The second element of big_list is list4. Display big_list.

big_list = [list3, list4]
print('Big List:')
print(big_list)

# (h) [2 points] Use a set of nested loops to display every number in big_list in a separate line.
# Since there are 12 numbers in big_list, 12 lines of output should be generated.

print('Big List Values:')
for r in range(2):
    for c in range(6):
        print(big_list[r][c])

# (i) [2 points] Use list comprehension to select all the odd integers from list3. Store the result in a list.
# Display this list of odd integers.

comp_list1 = [x for x in list3 if x % 2 != 0]
print('List Comprehension - Odd numbers in List 3:')
print(comp_list1)

# (j) [2 points] Use list comprehension to select all the even integers from list4. Store the result in a list.
# Display this list of even integers.

comp_list2 = [x for x in list4 if x % 2 == 0]
print('List Comprehension - Even numbers in List 4:')
print(comp_list2)
