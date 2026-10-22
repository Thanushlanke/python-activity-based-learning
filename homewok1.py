# Question: Progressive Electricity Billing - Calculate household bills using multiple consumption slabs and fixed charges.
units = int(input("Enter units consumed: "))
fixed_charge = 50

if units <= 100:
    bill = (units * 2.0) + fixed_charge
elif units <= 200:
    bill = (100 * 2.0) + ((units - 100) * 3.5) + fixed_charge
else:
    bill = (100 * 2.0) + (100 * 3.5) + ((units - 200) * 5.0) + fixed_charge

print("Total Electricity Bill: Rs.", bill)