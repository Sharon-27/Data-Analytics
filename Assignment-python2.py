'''
---- THE BMI CALCULATIONS:-
'''
name = input("Enter name:")
weight = float(input("Enter weight in kg:"))
height = float(input("Enter height:"))
unit = input("Enter unit(cms/feet):").lower()

if weight<=0 or height <0:
    print("Enter positive values only")
elif unit == "cms":
    if 50 <= height <=250:
        height = height /100
    else:
        print("Invalid height")
        height = 0
elif unit == "feet":
    if 2 <= height <=8:
        height = height*0.3048
    else:
        print("Invalid height")
        height = 0
else:
    print("Enter only cms or feet")
    height = 0
if height > 0:
    bmi = weight/(height**2)
    if bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Healthy"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    print(f"{name} is {result}.BMI = {bmi:.2f}")
