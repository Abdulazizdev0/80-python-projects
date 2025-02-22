a = int(input('a sonini kiriting: '))
b = int(input('b sonini kiriting: '))
c = int(input('c sonini kiriting: '))

if a < b and a < c:
    print(a)
elif b < a and b < c:
    print(b)
else:
    print(c)