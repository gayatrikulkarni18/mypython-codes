class Numbers:
    multiplier=3
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        return self.x + self.y
    @classmethod
    def multiply(cls,a):
        return cls.multiplier*a
    @staticmethod
    def subtract(b,c):
        return b-c
    @property
    def value(self):
        return(self.x,self.y)
    @value.setter
    def value(self,xy_tuple):
        self.x,self.y=xy_tuple
    @value.deleter
    def value(self):
        del self.x
        del self.y
T=Numbers(2,4)
print(T.add())
print(T.subtract(7,4))
print(T.multiply(2))
print(Numbers.subtract(4,3))
