# Question: Multi-Product Shopping Budget Constraint - Evaluate a shopping basket containing multiple products and check budget.
budget = float(input("Enter total budget: "))
item1_price = float(input("Enter price of item 1: "))
item2_price = float(input("Enter price of item 2: "))

total_cost = item1_price + item2_price
print("Total Cost:", total_cost)

if total_cost <= budget:
    print("Purchase is within your budget!")
else:
    print("Budget exceeded! Reduce items.")