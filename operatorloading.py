class Demo:
    def __init__(self,age):
        self.age = age
    def __init__(self):
        return "age is {self.age}"
    def __add__(self,other):
        return self.age + other.age
d  = Demo(24)
d = Demo(30)
print(d)
print(d1)
print(d + d1)