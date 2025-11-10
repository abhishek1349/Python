#temperature converter usnig if-else statements
unit=input("is the temperature in celcius or fahrenheit(C or F): ")
temp=float(input ("Enter the temperature: "))
if unit=="C":
    temp=round((9*temp)/5 + 32, 2)
    print(f"The temperature in fahrenheit is: {temp} F")
elif unit=="F":
    temp=round((5*(temp-32))/9, 2)
    print(f"The temperature in celcius is: {temp} C")
else:
    print("Invalid unit")