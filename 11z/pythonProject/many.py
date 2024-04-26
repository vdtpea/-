num_grades = int(input("Enter the number of grades: "))
grades = []

for _ in range(num_grades):
    grade = float(input("Enter a grade: "))
    grades.append(grade)

print("Grades entered:")
for grade in grades:
    print(grade)

average_grade = sum(grades) / num_grades
print("Average grade: {:.2f}".format(average_grade))
