
n = int(input('nechta son kiritmoqchisz: '))
birinchi = int(input('birinchi son: '))

max = birinchi
min = birinchi

max_index = 1
min_index = 1

for i in range(2,n+1):
    sonlar = int(input(f'{i} sonni kiriting: '))

    if sonlar >= max:
        max = sonlar
        max_index = i
    if sonlar < min:
        min = sonlar
        min_index = i

print(f'{n}ta sonlardan kattasi {max} tartib raqami {max_index},eng kichigi {min} tartib raqami {min_index}')
