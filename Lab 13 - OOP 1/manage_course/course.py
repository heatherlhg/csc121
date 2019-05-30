# --------------------------------------------------------
# Lab 13 - Course Size Management
# Heather Gates

# This the Course class constructor
# --------------------------------------------------------


class Course:

    def __init__(self, code, max_size):
        self.course_code = code
        self.max_class_size = max_size
        self.enrollment = 0

    def add_student(self):
        if self.enrollment < self.max_class_size:
            self.enrollment = self.enrollment + 1
            print('One student added.')
        else:
            print('Course already full.')


    def drop_student(self):
        if self.enrollment > 0:
            self.enrollment = self.enrollment - 1
            print('Once student dropped.')
        else:
            print('Course is empty.')
