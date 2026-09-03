import json

with open("student.json","r") as file:
    student = json.load(file)
print("修改前：",student)
student["score"] = 90
with open("student.json","w") as file:
    json.dump(student,file)
print("修改后：",student)


