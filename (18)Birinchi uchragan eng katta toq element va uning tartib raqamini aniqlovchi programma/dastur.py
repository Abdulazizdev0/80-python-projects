
n = int(input('nechta son kiritasz: '))
birinchi = int(input('1 - sonni kiriting: '))

max = None
max_index = -1

if birinchi % 2 != 0:
    max = birinchi
    max_index = 1

for i in range(2,n+1):
    sonlar = int(input(f'{i} - sonni kiriting: '))

    if sonlar % 2 != 0:
        if max is None or sonlar > max:
            max = sonlar
            max_index = i

if max is None:
    print(0)
else:
    print(max,max_index)


