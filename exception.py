try:

    class Demo:

            def disp(self):
                p = int(input("Enter the first number"))
                q = int(input("Enter the second number"))
                c = p / q
                print(c)
except:
            print("Exception is handled")
finally:
            print("Program got terminated1")
d =Demo()
d.disp()