class Singletion(object):


    instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
            return cls.instance


    def __init__(self, a, b):
        self.a = a
        self.b = b


s1 = Singletion("1","2")
s2 = Singletion("3","4")
print(s1 is s2)