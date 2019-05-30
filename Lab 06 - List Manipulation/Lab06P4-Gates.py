#Lab 06 - List Manipulation Problem 4 -
#Heather Gates

squares = [2**x for x in range(5) if x > 0]
print('Squares using list comprehension:', squares)

cubes = [3**x for x in range(5) if x > 0]
print('Cubes using list comprehension:', cubes)

matrix = [[2**x for x in range(5) if x > 0], [3**x for x in range(5) if x > 0], [4**x for x in range(5) if x > 0],
          [5**x for x in range(5) if x > 0], [6**x for x in range(5) if x > 0]]
print('Matrix of Powers:', matrix)

print('Matrix of Powers List')
for i in range(len(matrix)):
    print(matrix[i])

matrix_T = [[row[y] for row in matrix] for y in range(4)]
print('Transpose the matrix:', matrix_T)
