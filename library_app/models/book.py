class Book:
    def __init__(self,name:str,money:int):
        self.name = name
        self.money = money
    def introduce(self)->None:
        print("书名:",self.name)
        print("价格:",self.money)
