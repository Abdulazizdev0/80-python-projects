
n = int(input('nechta son kiritmoqchisz: '))
birinchi = int(input('1 - sonni kiriting: '))

max = birinchi
min = birinchi

max_index = 1
min_index = 1

for i in range(2,n+1):
    sonlar = int(input(f'{i} - sonni kiriting: '))
    if sonlar >= max:
        max = sonlar
        max_index = i
    if sonlar <= min:
        min = sonlar
        min_index = i

if max_index > min_index:
    print(max,max_index)
else:
    print(min,min_index)
