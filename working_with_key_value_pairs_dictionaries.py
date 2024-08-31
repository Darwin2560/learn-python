student = {"name": "Darwin", "age": 25, "courses": ["Math", "CompSci"]}

student["phone"] = "555-1234"
student["avatar"] = "👨‍💻"
student.update({"age": 24})
del student["phone"]
avatar = student.pop("avatar")
print(f"Avatar: {avatar}")
# print(student.get('phone', 'No phone number provided'))
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key, value in student.items():
    print(key, value)
