starter = int(input('summani kiriting: '))
p = int(input('foyizni kiriting: '))

current = starter
month = 0

while current <= 2 * starter:
    current += current * p / 100
    month += 1

print(f'{month} oyda {current} som')