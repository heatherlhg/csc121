output_file = open('my_file.txt', 'w')
my_list = ['apple', 'banana', 'orange']
for fruit in my_list:      
    output_file.write(fruit)
output_file.close()
