class Demo:
    def disp(self):
        print("1st method")
    def disp(self,a):
        print("2nd method")

    def disp(self,a,b):
        print("3rd method")
    def disp(self,a,b,c,d):
        print("100 rd method")
d = Demo()
# d.disp()
# d.disp(10)
# d.disp(10,20)
d.disp(1, 2, 3, 4)