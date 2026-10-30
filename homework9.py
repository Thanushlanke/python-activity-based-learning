# Question: Library Borrowing and Fine Reconciliation - Analyse book borrowing periods and calculate overdue fines.
# Library Borrowing and Fine Reconciliation
allowed_days = 10
actual_days = int(input("Enter actual days taken to return the book: "))

if actual_days <= allowed_days:
    print("Book returned on time. No fine!")
else:
    late_days = actual_days - allowed_days
    fine = late_days * 5
    print("Book is late by", late_days, "days.")
    print("Total Fine to Pay: ₹", fine)
