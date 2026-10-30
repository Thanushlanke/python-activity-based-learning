# Student Marks Matrix Analysis
print("Enter marks for 3 subjects:")
m1 = float(input("Subject 1 marks: "))
m2 = float(input("Subject 2 marks: "))
m3 = float(input("Subject 3 marks: "))
total = m1 + m2 + m3
average = total / 3
print("\n--- Results ---")
print("Total Marks:", total)
print("Average Marks:", round(average, 2))
if average >= 40:
    print("Status: Passed")
else:
    print("Status: Failed")
