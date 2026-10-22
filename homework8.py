# Question: Smart Canteen Order and Stock Management - Process successive customer orders, calculate bills, and update inventory.
stock = {"Burger": 10, "Pizza": 5, "Tea": 20}
price = {"Burger": 50, "Pizza": 120, "Tea": 15}

item = input("Enter item to buy (Burger/Pizza/Tea): ")
qty = int(input("Enter quantity: "))

if item in stock and stock[item] >= qty:
    stock[item] -= qty
    total_bill = price[item] * qty
    print("Order successful! Total Bill: Rs.", total_bill)
    print("Remaining stock for", item, ":", stock[item])
else:
    print("Sorry, item out of stock or invalid name.")