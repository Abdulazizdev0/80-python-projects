
n = int(input('nechta raqam kiritmoqchisz: '))
birinchi = int(input('1 - sonni kiriting: '))

min  = float('inf')

if birinchi > 0:
    min = birinchi

for i in range(2,n+1):
    sonlar = int(input(f'{i} - sonni kiriting: '))
    if 0 < sonlar < min:
        min = sonlar


if min == float('inf'):
    print(0)
else:
    print(min)