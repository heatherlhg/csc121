# Lab 08 - Functions - Problem 3
# Heather Gates

# The sample code.

print("This program creates a list of odd numbers in the range of your choice.")
start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))
my_list = []
for i in range(start_num, end_num+1):
    if i % 2 == 1:
        my_list.append(i)
print("odd numbers in the range:", my_list)

# Generator code.
# I was confused about "no loop being allowed", but both the generator example and the list comprehension contain loops.
# I went with the list comprehension since it was cleaner.

print("This program creates a list of odd numbers in the range of your choice.")
start_num = int(input("Enter starting number: "))
end_num = int(input("Enter ending number: "))
odd_list = list(i for i in range(start_num,end_num+1) if i % 2 == 1)
print("odd numbers in the range:", odd_list)
