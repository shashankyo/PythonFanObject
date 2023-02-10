# Generation of ecxeption
# class Demo:
#     def add(self):

#         try:
#             a =int(input("Enter the value of a"))
#             b =int(input("Enter the value of b "))
#             c=a/b
#             print(c)
#         except:
#             print("Error handled successfully")
# d = Demo()
# d.add()

# Generation of Exception
# def alpha():
#     print("Connection 3 has started")
#     a = 10
#     b = 2
#     c = a/b
#     print(c)
#     print("Connection 3 has ended")
# def beta():
#     print("Connection 2 started")
#     alpha()
#     print("Connection 2 terminated")
# def gamma():
#     print("Connection 1 started")
#     beta()
#     print("Connection 1 ended")
# gamma()
# Handling of the above Exception
# def alpha():
#     print("Connection 3 is started")
#     try:
#         a=int(input("Enter the first number"))
#         b =int(input("Enter the second number"))
#         c = a/b
#         print(c)
#     except:
#         print("Exception is handled")
#     print("Connection 3 ended")

# def beta():
#     print("Connection 2 started")
#     alpha()
#     print("Connection 2 ended")
# def gamma():
#     print("Connection 1 started")
#     beta()
#     print("Connection 1 terminated")
# gamma()

# Try, Except and Finally keyword
# def fun():
#     try:
#         numerator = int(input("Enter the numerator value"))
#         denominator = int(input("Enter the denominator value"))
#         result = numerator / denominator
#         print(result)
#     except:
#         print("Exception is handled")
#     finally:
#         print("Final statement")
# print("Program started")

# fun()
# print("Program is terminated")

# Try, except, else and finally keyword
# def fun():
#     try:
#         numerator = int(input("Enter the numerator value"))
#         denominator = int(input("Enter the denominator value"))
#         result = numerator/denominator
#         print(result)
#     except:
#         print("Exception is handled")
#     else:
#         print("Else block is getting executed")
    
#     finally:
#         print("Final statement")

# print("Program started")
# fun()
# print("Program is executed ")

# Advantage of using multiple except block

def fun():
    try:
        numerator = int(input("Enter the numerator"))
        denominator = int(input("Enter the denominator value"))
        result = numerator / denominator
        print(result)
    except ZeroDivisionError:
        print("Zero error error has occured")
    except ValueError:
        print("Value error exception occured")
    else:
        print("No exception has occured")
    finally:
        print("Finally block is executed")
print("Program has started")
fun()
print("Program is ended")