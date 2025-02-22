number = int(input('sonni kiriting: '))
sonlar = number
digit_count = 0
digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number = number // 10
    digit_count += 1

print(f'{sonlar} kiritgan soningizni {digit_count} honali ularni yegindisi {digit_sum}')