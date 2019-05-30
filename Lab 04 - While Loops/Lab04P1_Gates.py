#Lab 04 - While Loops Problem 1 - Diabetes Determination
#Heather Gates

another_patient = 'y'
another_patient = another_patient.lower()

while another_patient =='y':
    fpg = float(input("Please enter the patient's Fasting Plasma Glucose (FPG) level: "))
    if fpg >= 125:
        print("The FPG entered was:", fpg)
        print("The patient has diabetes.")
    elif fpg >= 100 and fpg < 125:
        print("The FPG entered was:", fpg)
        print("The patient has pre-diabetes.")
    else:
        print("The FPG entered was:", fpg)
        print("The patient is healty.")
    another_patient = input("Would you like to test another patient's FPG level? [y/n] ")
