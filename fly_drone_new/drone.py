# --------------------------------------------------------
# Lab 13 - fly_drone Project - New
# Heather Gates

# This contains the drone class constructor
# --------------------------------------------------------


class Drone:

    def __init__(self):
        """ establish variables """
        self.__speed = 0.0
        self.__height = 0.0

    def accelerate(self):
        """ accelerate the drone """
        self.__speed = self.__speed + 10


    def decelerate(self):
        """ decelerate the drone. validate that it's going fast enough """
        if self.__speed >= 10:
            self.__speed = self.__speed - 10
        else:
            print('ERROR: You are not going fast enough to slow down.')

    def ascend(self):
        """ ascend the drone """
        self.__height = self.__height + 10

    def descend(self):
        """ descend the drone. validate that is is high enough """
        if self.__height >= 10:
            self.__height = self.__height - 10
        else:
            print('ERROR: You are not high enough to descend.')

    def __str__(self):
        return 'Speed: ' + str(self.__speed) + '  Height: ' + str(self.__height)
