# Lab 07 - Functions - Problem 4
# Heather Gates

def main():
    lab_scores = []
    l = int(input('How many labs are there? '))
    while l > 0:
        lab = float(input('Enter a lab score: '))
        lab_scores.append(lab)
        l = l -1

    print('Lab scores: ', lab_scores)

    test_scores = []
    t = int(input('How many tests are there? '))
    while t > 0:
        test = float(input('Enter a test score: '))
        test_scores.append(test)
        t = t - 1

    print('Test scores: ', test_scores)

    print('Default weight is: tests = 50% and labs = 50%')
    weight_type = input('Do you want to accept default weights (D) or customize (C)? ')
    weight_type = weight_type.upper()
    while weight_type != 'D' and weight_type != 'C':
        print('ERROR: Please enter either D or C')
        weight_type = input('Do you want to accept default weights (D) or customize (C)? ')
        weight_type = weight_type.upper()

    if weight_type == 'D':
        grade_calculator(lab_scores, test_scores, lab_weight = 50, test_weight = 50)
    else:
        lab_weight = int(input('What is the weight of labs? '))
        test_weight = int(input('What is the weight of tests? '))
        while lab_weight + test_weight != 100:
            print('ERROR: lab and test weights must total 100')
            lab_weight = int(input('What is the weight of labs? '))
            test_weight = int(input('What is the weight of tests? '))
        grade_calculator(lab_scores, test_scores, lab_weight, test_weight)

def grade_calculator(lab_scores, test_scores, lab_weight, test_weight):

    lab_sum = 0
    for l in lab_scores:
        lab_sum = lab_sum + l
    lab_avg = lab_sum / len(lab_scores)

    print('The average of lab scores is: ', format(lab_avg, '.2f'))

    test_sum = 0
    for t in test_scores:
        test_sum = test_sum + t
    test_avg = test_sum / len(test_scores)

    print('The average of test scores is: ', format(test_avg, '.2f'))

    test_grade = test_avg * (test_weight/100)
    lab_grade = lab_avg * (lab_weight/100)

    print('Lab grade is: ', format(lab_grade, '.2f'))
    print('Test grade is: ', format(test_grade, '.2f'))

    course_grade = lab_grade + test_grade

    print('Course grade is: ', course_grade)

main()
