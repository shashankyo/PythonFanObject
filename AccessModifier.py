# public access modifier
class Demo:
    def __init__(self):
        self.x = 10
        self.y = 20
class Test:
    def disp(self):
        d1 = Demo()
        print(d1.x)
        print(d1.y)

d = Demo()
print(d.x)
print(d.y)
t = Test()
t.disp()

# Protected access modifier
class Demo:
    def __init__(self):
        self._x = 10
        self._y = 20

class Test:
    def disp(self):
        d1 = Demo()
        print(d1._x)
        print(d1._y)
d =Demo()
t =Test()
t.disp()
# Private access keyword
class Demo:
    def __init__(self):
        self.__x = 10
        self.__y = 20
d = Demo()
print(d._Demo__x)
print(d._Demo__y)
