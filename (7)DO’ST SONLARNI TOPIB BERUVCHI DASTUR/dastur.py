n = int(input('n kiriting: '))

def sum_of_devisor(number):
    total = 0
    for i in range(1,number):
        if number % i == 0:
            total += i
    return total

amicable_pairs = []

for a in range(1,n + 1):
    b = sum_of_devisor(a)
    if a < b <= n and a == sum_of_devisor(b):
        amicable_pairs.append((a,b))

for pair in amicable_pairs:
    print(pair[0],pair[1])