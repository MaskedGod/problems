students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], 
            ['Akriti', 41], ['Harsh', 39]]

scores = []

print(students)
for student in students:
    scores.append(student[1])

lowest2 = sorted(set(scores))[1]
print(lowest2)

for student in sorted(students):
    if student[1] == lowest2:
        print(student[0])

