class Demo:
    def __init__(self):
        self.name = "kodnest"
        Demo.age = 25
    @staticmethod
    def staticmethod():
        Demo.course = "Python"
        Demo.goal = "job"
    @classmethod
    def classmethod(cls):
        print("Inside the class method")
        cls.marks = 80
    
    def main():
        d =Demo()
        d.staticmethod()
        d.classmethod()
        print(Demo.age)
        print(Demo.course)
        print(Demo.goal)
        print(Demo.marks)
    main()