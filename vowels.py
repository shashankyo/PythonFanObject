#counting no of vowels                              

# s = 'Shashank devadiga'
# s = s.upper()
# v = 0
# for i in s:
#     if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
#         v =v+1
# print("The count is ",v)


#counting no of special characters,vowels and consonants                              

s = 'Shashank@3devadiga...///'
s = s.upper()
v = 0
c = 0
sp = 0
for i in s :
    if i >='A' and i <='Z':
        if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
            v = v+1
        else:
            c = c+1
    else:
        sp = sp+1
print("The count vowel is ",v)
print("The count consonants is ",c)
print("The count special characters is ",sp)


