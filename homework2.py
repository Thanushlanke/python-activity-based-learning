# ATM Transaction Simulation
balance = 10000
print("Current Balance: ₹", balance)

amount = float(input("Enter amount to withdraw: "))

if amount <= balance:
    balance = balance - amount
    print("Withdrawal successful! Remaining Balance: ₹", balance)
else:
    print("Transaction Failed: Not enough balance!")
