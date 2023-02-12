class Demo:
    def __init__(self):
        self.name = "Kodnest"
        Demo.age = 25
    @staticmethod
    def staticmethod():
        Demo.course = "Python"
        Demo.goal = "job"
        Demo.marks = 49

    @classmethod
    def classmethod(cls):
        print("Inside the class method")
def main():
    d = Demo()
    d.staticmethod()
    d.classmethod()
    print(Demo.age)
    print(Demo.course)
    print(Demo.goal)
    print(Demo.marks)
main()
