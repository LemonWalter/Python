# import pythonFile

# print(pythonFile.PythonStudy.a)



class Lemon():
    type1 = "人类"
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self, food):
        print(self.name, self.age, food)

    @classmethod
    def eatFood(cls):
        print(cls.type1)

Lemon.eatFood()
