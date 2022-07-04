from collections import defaultdict

exam_grades = [
    ("Bob", 100), ("Joe", 92), ("Emily", 95), ("Bob", 85), ("Joe", 87), ("Emily", 91)
]

student_grades = defaultdict(list)

for name, grade in exam_grades:
    student_grades[name].append(grade)

print(student_grades)

print(student_grades["Rob"])