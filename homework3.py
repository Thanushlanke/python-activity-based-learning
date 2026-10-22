# Question: Attendance Recovery Computation - Calculate current attendance percentage and check eligibility threshold.
attended = int(input("Enter classes attended: "))
total = int(input("Enter total classes held: "))

percentage = (attended / total) * 100
print(f"Current Attendance: {percentage:.2f}%")

if percentage >= 75:
    print("Eligible for exams.")
else:
    print("Attendance shortage! Needs improvement.")