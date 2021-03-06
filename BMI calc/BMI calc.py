import math


# Performs calculation
def data():
    height = input("Enter your height in inches: ")
    weight = input("Enter your weight in lbs: ")
    status = ()
    bmi = int(weight) / int(height) ** 2 * 703
    if bmi <= 18:
        status = "underweight"
    elif bmi <= 24 or bmi >= 19:
        status = "healthy"
    elif bmi <= 25 or bmi >= 29:
        status = "overweight"
    elif bmi <= 39 or bmi >= 30:
        status = "obese"
    elif bmi > 39:
        status = "extremely obese"
    print("Your BMI is " + str(math.floor(bmi)))
    print("You are " + status)


# restarts the calc
def retry():
    redo = input("Enter y to continue: ")
    if redo == "y":
        return beginning()
    else:
        print("Have a nice day!")


# allows looping to work
def beginning():
    data()
    retry()


beginning()
