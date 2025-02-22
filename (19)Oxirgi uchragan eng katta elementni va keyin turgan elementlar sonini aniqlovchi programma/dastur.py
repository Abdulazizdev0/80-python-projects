
n = int(input('nechta son kiritasiz?: '))
birinchi = int(input('1 - sonni kiriting: '))

max = birinchi
max_index = 1

for i in range(2,n+1):
    sonlar = int(input(f'{i} - sonni kiriting: '))

    if sonlar >= max:
        max = sonlar
        max_index = i

next_elements_count = n - max_index

print(f'eng katta son {max},next_element counts {next_elements_count}')