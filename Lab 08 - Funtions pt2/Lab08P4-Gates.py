# Lab 08 - Functions - Problem 4
# Heather Gates

# Sample code.

print('Using original code')


def average (my_list) :
    avg = sum(my_list)/len(my_list)
    return avg


list1 = [2, 1, 5, 9, 8]
list1_avg = average(list1)
print("list1 average:", format(list1_avg,".2f"))
list2 = [17, 5, 2, 4]
list2_avg = average(list2)
print("list2 average:", format(list2_avg,".2f"))


# Lambda code.

print('Using lambda function')
list_avg = lambda my_list: sum(my_list)/len(my_list)
list1 = [2, 1, 5, 9, 8]
print("list1 average:", format(list_avg(list1),".2f"))
list2 = [17, 5, 2, 4]
print("list2 average:", format(list_avg(list2),".2f"))
