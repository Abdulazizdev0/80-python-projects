
n = int(input('nechta son kiritasz: '))

first_number = int(input('1 - sonni kiriting: '))
second_number = int(input('2 - sonni kiriting: '))

max_sum = first_number + second_number
prev_number = second_number

for i in range(3,n+1):
    sonlar = int(input(f'{i} - sonni kiriting: '))

    sonlar_sum = prev_number + sonlar

    if sonlar_sum > max_sum:
        max_sum = sonlar_sum
    prev_number = sonlar

print(max_sum)