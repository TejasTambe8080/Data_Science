students = {
    "A": 80,
    "B": 40,
    "C": 90
}

topper = max(students, key=students.get)
print("Topper:", topper)