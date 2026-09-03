from models.student import Student

def is_pass(student:Student,pass_score:int = 60)->bool:
    return student.score >= pass_score