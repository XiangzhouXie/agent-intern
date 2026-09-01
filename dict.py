students={
    "alice":85,
    "bob":55,
    "charlie":78,
    "david":92
}
for name,score in students.items():
    print(name,score)
for name,score in students.items():
    if score>=60:
        print(name,score)
for name,score in students.items():
    if score<60:
        print(name,score)
    
max_score = 0
best_student = ""
for name,score in students.items():
    if score>max_score:
        max_score =  score
        best_student = name
print(best_student,max_score)
