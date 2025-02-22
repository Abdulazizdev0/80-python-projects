

soni = int(input('sonini kiriting: '))
birinchi_son = int(input('sonlarni kiriting: '))

max = birinchi_son
min = birinchi_son

for i in range(soni-1):
    son = int(input('keyingi sonni kiriting: '))
    if son > max:
        max = son
    if son < min:
        min = son

print(f'{soni} sondan kattasi {max},kichkinasi {min}')
