# Multiple Inheritence
# class Parent1:
#     def disp(self):
#         print("1st method")
# class Parent2:
#     def disp1(self):
#         print("2nd method")
# class child(Parent1,Parent2):
#     pass
# c = child()
# c.disp1()
# c.disp()
#  Multilevel Inheritence
# class Parent1:
#     def disp(self):
#         print("1st method in parent class")
# class Parent2(Parent1):
#     def disp1(self):
#         print("First method in parent 2 class")
# class child(Parent2):
#     def disp2(self):
#         print("First method of child class")
# c = child()
# c.disp()
# c.disp1()
# c.disp2()
# Heirarchial inheritance
class Parent1:
    def disp(self):
        print("First method in parent class")
class child1(Parent1):
    def disp1(self):
        print("First method in child1 class")
class child2(Parent1):
    def disp(self):
        print("First method in child2 class")
c1 = child1()
c1.disp()
c1.disp1()
c2 = child2()
c2.disp()
