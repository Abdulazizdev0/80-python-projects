

n = int(input('n kiriting: '))
prime_numbers = []
for number in range(2,n+1):
    is_prime = True
    for devisor in range(2,number):
        if number % devisor == 0:
            is_prime = False
    if is_prime:
        prime_numbers.append(number)
print(prime_numbers)