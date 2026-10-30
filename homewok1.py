
# Progressive Electricity bill
units = float(input("Enter units consumed: "))

if units <= 100:
    total = units * 2.0
elif units <= 300:
    total = (100 * 2.0) + ((units - 100) * 3.5)
else:
    total = (100 * 2.0) + (200 * 3.5) + ((units - 300) * 5.0)

print("Total Electricity Bill: ₹", round(total, 2))
