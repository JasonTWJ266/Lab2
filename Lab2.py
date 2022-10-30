def calculate_bmi(weight,height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight/(height*height)
    if(bmi < 18.5):
        return f'You have a BMI rating of {bmi}.You are underweight'
    elif(bmi <=18.5 and bmi <=25):
        return f'You have a BMI rating of{bmi}.You have a normal weight'
    else:
        return f'You have a BMI rating of {bmi}.You are overweight'
print(calculate_bmi(57,1.73))