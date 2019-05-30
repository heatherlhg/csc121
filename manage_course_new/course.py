# --------------------------------------------------------
# Lab 13 - Course Size Management
# Heather Gates

# This the Course class constructor
# --------------------------------------------------------


class Course:

    def __init__(self, code, max_size):
        self.__course_code = code
        self.__max_class_size = max_size
        self.__enrollment = 0

    def add_student(self):
        if self.__enrollment < self.__max_class_size:
            self.__enrollment = self.__enrollment + 1
            print('One student added.')
        else:
            print('Course already full.')

    def drop_student(self):
        if self.__enrollment > 0:
            self.__enrollment = self.__enrollment - 1
            print('Once student dropped.')
        else:
            print('Course is empty.')

    def getCode(self):
        return self.__course_code

    def getMax(self):
        return self.__max_class_size

    def getEnrollment(self):
        return self.__enrollment

    def setMaxsize(self, max_size):
        if max_size < 0:
            print('ERROR: Maxmium class size cannot be negative.')
        elif max_size < self.__enrollment:
            print('ERROR: Maximum class size cannot be lower than current enrollment.')
        else:
            self.__max_class_size = max_size
