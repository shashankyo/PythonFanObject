class Parent:
    def __init__(self):
        print("Parent class constructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child class constructor")
        # super().__init__()
        # super().__init__()
c = Child()