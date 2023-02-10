# class demo:
#     def __init__(self):
#         print("Inside the constructor")
# d = demo()
# print(d)

# class Demo:
#     def __init__(self):
#         self.name = "kodnest"
#     def __str__(self):
#         return self.name
# d = Demo()
# print(d)

# Magic method example
class Circle:
    def __init__(self,radius):
        self.radius = radius
    def __add__(self,other):
        return self.radius + other.radius
    def __sub__(self,other):
        return self.radius - other.radius
    def __mul__(self,other):
        return self.radius*other.radius
    def __div__(self,other):
        return (self.radius * other.radius)
    def __lt__(self,other):
        return self.radius < other.radius
    def __gt__(self,other):
        return self.radius > other.radius
def main():
    c1 = Circle(4)
    c2 = Circle(10)
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)  
    print(c1 * c2)
    print(c1 < c2)
    print(c1 > c2)
main()