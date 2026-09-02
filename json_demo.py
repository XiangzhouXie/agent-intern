import json
json_text = '{"name":"Alice","age":20,"score":85}'
print(type(json_text))
student = json.loads(json_text)
print(student)
print(type(student))
print(student["name"])
student2 = {"name":"Bob","age":21,"score":90}
json_text2 = json.dumps(student2)
print(json_text2)
print(type(json_text2))
