class Student:
    def __init__(self, name:str,age:int,score:int):
        self.name = name
        self.age = age
        self.score = score
    def introduce(self)->None:  
        print("My name is",self.name)
        print("My score is",self.score)