def decor(function):
    def inner(name):
        if name == "Sachin":
            print(name,"get cheez burst pizza")
        else:
            function(name)
        return inner

@decor
def pizza(name):
    print(name,"gets hand made pizza")

pizza("Praveen")
pizza("Sachin")
pizza("Shiva")