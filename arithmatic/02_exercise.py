import math
#to find hypotenuse of right angled triangle
a=float(input("Enter length of side a: "))
b=float(input("Enter length of side b: "))
#c=math.sqrt(a**2 + b**2)
c=math.sqrt(pow(a,2) + pow(b,2))
#print("The length of hypotenuse is:",c)
print(f"The length of hypotenuse c is : {c}")