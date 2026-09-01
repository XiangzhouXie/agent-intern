students: dict[str,int] = {
    "alice": 85,
    "bob": 55,
    "charlie": 78,
    "david": 92
}
def print_all_students(students:dict[str,int])->None:
    # 这里你自己写
    for name,score in students.items():
        print(name,score)
def print_pass_students(students:dict[str,int])->None:
    # 这里你自己写
    for name,score in students.items():
        if score>=60:
            print(name,score)
print_pass_students(students)
print_all_students(students)
def get_best_student(students:dict[str,int])->tuple[str,int]:
    # 这里你自己写
    max_score = 0
    best_student = ""
    for name,score in students.items():
        if score>max_score:
            max_score =  score
            best_student = name
    return best_student,max_score
best_student ,max_score = get_best_student(students)
print(best_student,max_score)
# 练习2
def print_passed_students(students:dict[str,int], pass_score:int = 60)->None:
    # 这里你自己写
    for name,score in students.items():
        if score>=pass_score:
            print(name,score)
            
print_passed_students(students)
print_passed_students(students,90)