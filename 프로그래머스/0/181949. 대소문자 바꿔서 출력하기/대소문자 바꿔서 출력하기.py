str = input()
b = ''
for i in str:
    if i.isupper():
        b += i.lower()
    elif i.islower():
        b += i.upper()
        
print(b)
        
        