def disp():
    yield 1
    yield True
    yield 3
    yield "shashank"

res = disp()
print(res.__next__())
print(res.__next__())
print(res.__next__())
print(res.__next__())
