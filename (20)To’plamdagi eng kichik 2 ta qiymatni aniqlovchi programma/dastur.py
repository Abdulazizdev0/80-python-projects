
n = int(input('nechta son kiritasiz: '))
first_number = int(input('1 - sonni kiriting: '))
second_number = int(input('2 - sonni kiriting: '))

if first_number < second_number:
    min1,min2 = first_number,second_number
else:
    min1,min2 = second_number,first_number

for i in range(3,n+1):
    sonlar = int(input(f'{i} - sonni kiriting: '))

    if sonlar < min1:
        min2 = min1
        min1 = sonlar
    elif sonlar < min2:
        min2 = sonlar

print(min1,min2)

