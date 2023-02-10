lst = [1,2,3,4,5,6,7,8,9]
new_lst = list(filter(lambda num:num%2 == 0,lst))
print(lst)
print(new_lst)

lst = [9,8,7,6,5,4,3,2,1]
new_lst = list(map(lambda num:num **2, lst))
print(lst)
print(new_lst)