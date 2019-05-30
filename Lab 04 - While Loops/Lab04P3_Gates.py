#Lab 04 - While Loops Problem 3 - Bouncing Ball
#Heather Gates

num_bounces = int(input("How many times should the ball bounce? "))
initial_height = float(input("What is the initial height the ball is dropped from? "))
first_bounce = float(input("What is the height of the first bounce? "))
bounce_ratio = first_bounce / initial_height
print("You entered an initial drop height of: ", initial_height, "and a first bounce height of: ", first_bounce)
print("The bounciness ratio is: ",bounce_ratio)
while num_bounces > 0:
    remaining_bounce = (first_bounce * bounce_ratio)
    print("Bounce countdown:", num_bounces, " Bounce height:", format(remaining_bounce, ".2f"))
    first_bounce = remaining_bounce
    num_bounces = num_bounces - 1
