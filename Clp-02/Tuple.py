students = (
    ("Razin", 24, 3.5),
    ("Tawhid", 23, 3.25),
    ("Sahim", 25, 3.4),
    ("Mrinmoy", 22, 3.3)
)

Sorted = sorted(students, key=lambda student: student[2])
print("Student Sorted By Grade: ",Sorted)