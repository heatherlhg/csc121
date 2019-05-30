# --------------------------------------------------------
# Lab 13 - fly_drone Project
# Heather Gates

# This contains the main function
# --------------------------------------------------------


from drone import Drone


def main():
    flight = Drone()
    operation = 0
    while operation != 5:
        operation = int(input('Enter a diretion: 1 to accelerate, 2 to decelerate, 3 to ascend or 4 to descend. Enter 5 to exit. '))
        while operation < 1 or operation > 5:
            print('ERROR: Operation not recognized. ')
            operation = int(input('Enter a diretion: 1 to accelerate, 2 to decelerate, 3 to ascend or 4 to descend. Enter 5 to exit. '))
        if operation == 1:
            flight.accelerate()
            print('Speed: ', flight.speed, 'Height: ', flight.height, '\n')
        elif operation == 2:
            flight.decelerate()
            print('Speed: ', flight.speed, 'Height: ', flight.height, '\n')
        elif operation == 3:
            flight.ascend()
            print('Speed: ', flight.speed, 'Height: ', flight.height, '\n')
        elif operation == 4:
            flight.descend()
            print('Speed: ', flight.speed, 'Height: ', flight.height, '\n')
        else:
            print('You have exited the program.')


main()
