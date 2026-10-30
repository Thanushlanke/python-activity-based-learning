# Employee Payroll and Deduction Analysis`
basic = float(input("Enter Basic Salary: "))
hra = float(input("Enter HRA: "))

gross = basic + hra
pf = basic * 0.12
net = gross - pf

print("Gross Salary: ₹", gross)
print("PF Deduction: ₹", pf)
print("Net Salary: ₹", net)
