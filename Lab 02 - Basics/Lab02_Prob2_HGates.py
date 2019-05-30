## Calculate lab and test average. Calculate course grade.

lab1 = float(input('Enter the grade for Lab 1 '))
lab2 = float(input('Enter the grade for lab 2 '))
lab3 = float(input('Enter the grade for lab 3 '))

test1 = float(input('Enter the grade for test 1 '))
test2 = float(input('Enter the grade for test 2 '))

lab_average = (lab1 + lab2 + lab3)/3
test_average = (test1 + test2)/2

course_grade = (lab_average * 0.55)+(test_average * 0.45)

print('Lab Average:',lab_average)
print('Test Average:',test_average)
print('Course Grade:',course_grade)
