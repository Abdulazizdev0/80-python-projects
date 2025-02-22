
n = int(input('nechta son kiritmoqchisiz: '))
birinchi = int(input('birinchi son: '))

min = birinchi
index = 1

for i in range(n-1):
    sonlar = int(input('keyingi sonlarni kiriting: '))
    index += 1
    if sonlar < min:
        min = sonlar


print(f'{n}ta kiritgan sonlarizdan eng kichigi {min},  {index}chi raqam')

