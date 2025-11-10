#Shopping cart program
item=input("Enter the item you want to buy: ")
price=float(input("Enter the price of the item: "))
quantity=int(input("Enter the quantity: "))
total=price*quantity
print(f"You have purchased {quantity} x{item}/s")
print("Total price is: $", total)