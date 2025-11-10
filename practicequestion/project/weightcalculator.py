weight=float(input("Enter your weight: "))
unit=input("Enter unit (kg or lb): ")
if unit=="kg":
    weight=weight*2.205
    unit="lbs"
    print(f"You weight {round(weight, 1)} {unit}")
elif unit=="lb":
    weight=weight/2.205
    unit="kgs"
    print(f"You weight {round(weight, 1)} {unit}")
else:
    print("Invalid unit")