class Addition:
    def add(self,a,b):
        print(a+b)
class Subtraction:
    def sub(self,a,b):
        print(a-b)
class Multiplication:
    def mul(self,a,b):
        print(a*b)
class Division:
    def div(self,a,b):
        print(a/b)
def Calculator(ref,a,b):
    if type(ref).__name__ == 'Addition':
        ref.add(a,b)
    elif type(ref).__name__ == 'Subtraction':
        ref.sub(a,b)
    elif type(ref).__name__ == 'Multiplication':
        ref.mul(a,b)
    elif type(ref).__name__ == 'Division':
        ref.div(a,b)
def main():
    ad = Addition()
    s = Subtraction()
    m = Multiplication()
    d = Division()
    x = int(input("Enter the first number"))
    y = int(input("Enter the second number"))
    Calculator(ad, x, y)
    Calculator(s, x, y)
    Calculator(m, x, y)
    Calculator(d, x, y)
main()