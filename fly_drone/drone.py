# --------------------------------------------------------
# Lab 13 - fly_drone Project
# Heather Gates

# This contains the drone class constructor
# --------------------------------------------------------


class Drone:

    def __init__(self):
        """ establish variables """
        self.speed = 0.0
        self.height = 0.0

    def accelerate(self):
        """ accelerate the drone """
        self.speed = self.speed + 10


    def decelerate(self):
        """ decelerate the drone. validate that it's going fast enough """
        if self.speed >= 10:
            self.speed = self.speed - 10
        else:
            print('ERROR: You are not going fast enough to slow down.')

    def ascend(self):
        """ ascend the drone """
        self.height = self.height + 10

    def descend(self):
        """ descend the drone. validate that is is high enough """
        if self.height >= 10:
            self.height = self.height - 10
        else:
            print('ERROR: You are not high enough to descend.')
