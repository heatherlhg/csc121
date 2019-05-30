# --------------------------------------------------------
# Lab 13 - fly_drone Project - New
# Heather Gates

# This contains the main function
# --------------------------------------------------------


from drone import Drone


def main():
    flight = Drone()
    operation = 0
    while operation != 5:
        operation = int(input('Enter a direction: 1 to accelerate, 2 to decelerate, 3 to ascend or 4 to descend. Enter 5 to exit. '))
        while operation < 1 or operation > 5:
            print('ERROR: Operation not recognized. ')
            operation = int(input('Enter a direction: 1 to accelerate, 2 to decelerate, 3 to ascend or 4 to descend. Enter 5 to exit. '))
        if operation == 1:
            flight.accelerate()
            print(flight)
        elif operation == 2:
            flight.decelerate()
            print(flight)
        elif operation == 3:
            flight.ascend()
            print(flight)
        elif operation == 4:
            flight.descend()
            print(flight)
        else:
            print('You have exited the program.')


main()
