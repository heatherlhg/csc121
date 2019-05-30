# Lab 11 - Dictionaries, Sets & Exceptions - Problem 2
# Heather Gates

# (a)	Generate 5 random integers between 1 and 10, inclusive.  Store the random integers in a set named set1.
# Display the set. Please note that the set may have less than 5 elements because some of the random integers
# generated may be redundant.

import random

set1 = set()
for i in range(5):
    num = random.randint(1,10)
    set1.add(num)
print('Set1: ', set1)

# (b)	Generate 5 random integers between 1 and 10, inclusive.  Store the random integers in another set named set2.
# Display the set. Please note that the set may have less than 5 elements because some of the random integers
# generated may be redundant.

set2 = set()
for i in range(5):
    num = random.randint(1,10)
    set2.add(num)
print('Set2: ', set2)

# (c) Find and display the union of set1 and set2.

set_union = set1 | set2
print('Set1 Union Set2: ', set_union)

# (d) Use set comprehension to select odd numbers from the union and store them in a set.  Display this set.

comp_set = {x for x in set_union if x % 2 != 0}
print('Odd numbers:', comp_set)

# (e)	Find and display the intersection of set1 and set2.

set_intersect = set1 & set2
print('Set1 intersect Set2: ', set_intersect)

# (f)	Find and display the symmetric difference of set1 and set2.

set_sym_dif = set1 ^ set2
print('Symmetric difference between Set1 and Set2: ', set_sym_dif)
