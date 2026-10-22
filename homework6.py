# Question: Employee Payroll and Deduction Analysis - Calculate gross salary from basic pay, allowances, and progressive tax deductions.
basic_pay = float(input("Enter basic pay: "))

hra = basic_pay * 0.20
da = basic_pay * 0.10
gross_salary = basic_pay + hra + da

if gross_salary <= 30000:
    tax = gross_salary * 0.05
elif gross_salary <= 60000:
    tax = gross_salary * 0.10
else:
    tax = gross_salary * 0.15

net_salary = gross_salary - tax
print("Gross Salary:", gross_salary)
print("Tax Deduction:", tax)
print("Net Salary:", net_salary)