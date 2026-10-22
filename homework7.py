# Question: Student Marks Matrix Analysis - Analyse a matrix of student marks across subjects and calculate row-wise totals and averages.
marks_matrix = [
    [75, 80, 85],
    [60, 65, 70],
    [90, 85, 95]
]

for i in range(len(marks_matrix)):
    total = sum(marks_matrix[i])
    avg = total / len(marks_matrix[i])
    print(f"Student {i+1} -> Total Marks: {total}, Average: {avg:.2f}")