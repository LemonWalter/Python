class Adog(object):

    def sttack(self):
        print("狗正在攻击坏人")

class police(object):

    def __init__(self, name):
        self.name = name

    def work(self):
        self.dog.sttack()

women = police("张三")

dog = Adog()
women.dog = dog
women.work()


dog = Adog()
women.dog = dog
women.work()

dog = Adog()
women.dog = dog
women.work()