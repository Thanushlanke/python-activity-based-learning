# Question: Library Borrowing and Fine Reconciliation - Analyse book borrowing periods and calculate overdue fines.
days_late = int(input("Enter number of days book is overdue: "))

if days_late <= 5:
    fine = days_late * 2
elif days_late <= 10:
    fine = (5 * 2) + ((days_late - 5) * 5)
else:
    fine = (5 * 2) + (5 * 5) + ((days_late - 10) * 10)

print("Total Library Fine: Rs.", fine)