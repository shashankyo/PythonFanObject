class Parent:
    def __init__(self):
        print("Parent class constructor")
    def cook(self):
        print("Parent is cooking Biryani")
class Child(Parent):
    def __init__(self):
        print("Child class constructor")
    def cook(self):
        print("Child class is cooking Maggie")
        super().cook()

c = Child()
c.cook()
