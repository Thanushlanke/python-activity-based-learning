# Smart Canteen Order and Stock Management
stock = 10
print("Available Burgers in Stock:", stock)

ordered = int(input("Enter number of burgers you want to buy: "))

if ordered <= stock:
    stock = stock - ordered
    print("Order successful!")
    print("Remaining stock in canteen:", stock)
else:
    print("Order failed! Not enough stock available.")
