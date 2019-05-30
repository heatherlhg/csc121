temp_list = []

for i in range(5):
    temp = float(input("Enter a temperature: "))
    temp_list.append(temp)

print()
print("Temperatures entered: ", temp_list)

temp_list.sort()
lowest_temp = temp_list[0]
highest_temp = temp_list[-1]
print("Lowest temperature:", lowest_temp)
print("Highest temperature:", highest_temp)

total = 0
for temp in temp_list:
    total = total + temp
avg_temp = total / 5
print("Average temperature:", avg_temp)

above_avg = 0
for temp in temp_list:
    if temp > avg_temp:
        above_avg = above_avg + 1
print("Number of days hotter than the average:", above_avg)

