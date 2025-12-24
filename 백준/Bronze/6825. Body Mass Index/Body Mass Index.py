a = float(input()) 
b = float(input()) 
BMI = a/(b * b)
if BMI > 25:
        print("Overweight")
elif 18.5 <= BMI <= 25:
        print("Normal weight")
else:
        print("Underweight")