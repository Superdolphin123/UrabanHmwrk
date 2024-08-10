grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
gpa = {}
students = sorted(list(students))
for i in range(len(grades)):
    grades[i] = sum(grades[i]) / len(grades[i])
for i in range(len(students)):
    for j in range(len(grades)):
        gpa.update({students[i]: grades[j]})
print(gpa)
