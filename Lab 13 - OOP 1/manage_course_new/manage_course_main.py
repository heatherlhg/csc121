# --------------------------------------------------------
# Lab 13 - Course Size Management
# Heather Gates

# This is the main function of course management
# --------------------------------------------------------

from course import Course

def main():
    course_code = input('Enter a course code: ')
    max_size = int(input('Enter the maximum class size: '))
    course_info = Course(course_code, max_size)
    i = 1
    while i != 0:
        course_action = int(input('Select a course action: 1 to add a student, 2 to drop a student, 3 to display course info or 4 to change class size. Type 0 to exit the program. '))
        while 0 > course_action or course_action> 4:
            print('ERROR: Please select a valid course action.')
            course_action = int(input('Select a course action: 1 to add a student, 2 to drop a student, 3 to display course info or 4 to change class size. Type 0 to exit the program. '))

        if course_action == 1:
            course_info.add_student()
            print('')
        elif course_action == 2:
            course_info.drop_student()
            print('')
        elif course_action == 3:
            print('Course code: ', course_info.getCode())
            print('Maximum class size: ', course_info.getMax())
            print('Enrollment: ', course_info.getEnrollment())
            print('')
        elif course_action == 4:
            max_size = int(input('Enter new maximum class size: '))
            course_info.setMaxsize(max_size)
            print('')
        elif course_action == 0:
            print('You have exited the program.')
            i = 0

main()
