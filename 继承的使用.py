# """
# 不使用继承的写法
# """
#
# class Animal(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(self.name + "正在睡觉")
#
# class Dog(object):
#
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(self.name + "正在睡觉")
#
#     def bark(self):
#         print(self.name + "正在叫")
#
#
# class Student(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(self.name + "正在睡觉")
#
#     def study(self):
#         print(self.name + "正在好好学习")


"""
使用继承的写法
"""

# class Animal(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         print(self.name + "正在睡觉")
#
# class Dog(Animal):
#
#     def __init__(self,name, age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def bark(self):
#         print(self.name + "正在叫")
#
#
# class Student(Animal):
#
#     def study(self):
#         print(self.name + "正在好好学习")
#
# animal1 = Animal("张三","18")
# dog2 = Dog("李四","22","女")
# student1 = Student("王五","81")
#
# animal1.sleep()
# dog2.bark()
# dog2.sleep()
# student1.sleep()
# student1.study()

#继承多个类,调用同名方法的顺序
class A(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age


class C(A):

    def __init__(self,name,age,school):

        #第一种重写父类的方式
        A.__init__(self,name,age)

        #第二种重写父类的方式
        super(C, self).__init__(name,age)

        self.school = school

c1 = C("1","2","3")