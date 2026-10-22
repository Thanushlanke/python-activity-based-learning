# Question: ATM Transaction Simulation - Process deposits and withdrawals, maintain simulated balance and check limits.
balance = 5000.0
print("Current Balance:", balance)

choice = input("Enter 'd' to deposit or 'w' to withdraw: ")
amount = float(input("Enter amount: "))

if choice == 'd':
    balance += amount
    print("Updated Balance:", balance)
elif choice == 'w' and amount <= balance:
    balance -= amount
    print("Updated Balance:", balance)
else:
    print("Invalid transaction or insufficient balance.")