from models.student import Student
from services.student_services import is_pass
from utils.formatter import format_student
alice = Student("Alice", 20, 85)
alice.introduce()
print(is_pass(alice))
text = format_student(alice.name,alice.score)
print(text)
