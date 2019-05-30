#Lab 05 - Lists & For Loops Problem 2 - Drop/Add Courses
#Heather Gates

courses = []
count_courses = len(courses)

# Initial input mode - Add, Drop, or Exit. Validate for correct input.
mode = input('Would you like to Add [a] or Drop [d] a course? Type [e] to exit? ')
mode = mode.lower()
while mode != 'a' and mode != 'd' and mode != 'e':
    print('Error: Please enter [a] to Add, [d] Drop, or [e] to exit')
    mode = input('Would you like to Add [a] or Drop [d] a course? Type [e] to exit? ')
    mode = mode.lower()

# Loop through drop/add modes based on input
while mode == 'd' or mode == 'a':
    while mode == 'd':
        if len(courses) == 0: # verify user has courses to drop
            print('Error: You are not registered for any courses yet. Please add a course.')
            mode = input('Would you like to Add [a] or Drop [d] a course? Type [e] to exit? ')
            mode = mode.lower()
        else:
            drop_course = str(input('Please enter the course number: '))
            while drop_course not in courses: # verify user is in chosen drop course
                print('Error: You are not registered in that course.')
                drop_course = str(input('Please enter the course number: '))
            courses.remove(drop_course)
            print('Course', drop_course, 'dropped.')
            courses.sort()
            print('You are registered for', len(courses), 'courses.')
            print('Your courses are:', courses)
            mode = input('Would you like to Add [a] or Drop [d] a course? Type [e] to exit? ')
            mode = mode.lower()
            while mode != 'a' and mode != 'd' and mode != 'e': # validate for correct input
                print('Error: Please enter [a] to Add, [d] Drop, or [e] to exit')
                mode = input('Would you like to Add [a] or Drop [d] a course? Type [e] to exit? ')
                mode = mode.lower()

    while mode == 'a':
        new_course = str(input('Please enter the course number: '))
        while new_course in courses: # verify user is not double registering for same course
            print('Error: You are already registered in that course.')
            new_course = str(input('Please enter the course number: '))
        courses.append(new_course)
        print('Course', new_course, 'added.')
        courses.sort()
        print('You are registered for', len(courses), 'courses.')
        print('Your courses are:', courses)
        mode = input('Would you like to Add [a] or Drop [d] a course? Type [e] to exit? ')
        mode = mode.lower()
        while mode != 'a' and mode != 'd' and mode != 'e': # validate for correct input
            print('Error: Please enter [a] to Add, [d] Drop, or [e] to exit')
            mode = input('Would you like to Add [a] or Drop [d] a course? Type [e] to exit? ')
            mode = mode.lower()

if mode == 'e': # exit the program upon drop/add completion. Summarize course selections.
    print('Thank you for using the course registration program.')
    if len(courses) > 0:
        print('You are registered for', len(courses), 'courses.')
        courses.sort()
        print('Your courses are:', courses)
