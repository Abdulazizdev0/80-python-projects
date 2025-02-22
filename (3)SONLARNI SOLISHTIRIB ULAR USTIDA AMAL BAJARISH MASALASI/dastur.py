x = int(input('x sonini kiriting: '))
y = int(input('y sonini kiriting: '))

min = (x + y) / 2
max = 2 * x * y

if x > y:
    x, y = max,min
elif x < y:
    x,y = min,max