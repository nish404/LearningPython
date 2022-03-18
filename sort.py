# sort() method = used with lists
# sort() function = used with iterables

# students = ["student1","student2","student3", "student4", "student5"]
students = ("student1","student2","student3", "student4", "student5")

# students.sort(reverse=True)
sorted_students = sorted(students, reverse=True)

for i in sorted_students:
    print(i)

students = [("student1", "pass", 70),
            ("student2", "fail", 30),
            ("student3", "pass", 88),
            ("student4", "fail", 60),
            ("student5", "pass", 100)]

grade = lambda grades:grades[1]
# students.sort(key=grade)
sorted_students = sorted(students,key=grade)

for i in sorted_students:
    print(i)
