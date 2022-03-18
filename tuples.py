# tuple = collection which is ordered and unchangeable used to group together related data 
student = ("jane doe",21,"female")

print(student.count("jane doe"))
print(student.index("female"))

for x in student:
    print(x)

if "jane doe" in student:
    print("jane doe is here")
