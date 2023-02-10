# # Python does not support Method Overloading
# class Demo:
#     def disp(self):
#         print("Inside first method")
#     def disp(self, a):
#         print("Inside second method")
#     def disp(self, a, b):
#         print("Inside third method")
#     def disp(self, a, b):
#         print("Inside third method")
# d = Demo()
# # d.disp(10,20)
# d.disp(10, 20)
# constructor Overloading
class Demo:
    def __init__(self):
        print("Inside first constuctor")
    def __init__(self, a):
        print("Inside second constructor")
    def __init__(self,a ,b):
        print("Inside third constructor")
d = Demo(10, 20)