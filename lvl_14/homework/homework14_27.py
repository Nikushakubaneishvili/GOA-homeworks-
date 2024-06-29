#lculate the BMI of a person based on their height and weight 
#entered by the user and classify their BMI category using if-else.
height=int(input("please enter your height: ") )
weight=int(input("please enter your weight: ") )
bmi=weight/height**2 
if bmi>=25:
    print("you are overweight") 
elif bmi<25 and bmi >18.5:
    print("you are normal") 
else:
    print("eat something :DD") 