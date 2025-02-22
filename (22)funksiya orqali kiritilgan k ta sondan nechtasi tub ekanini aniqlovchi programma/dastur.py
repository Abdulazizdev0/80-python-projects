
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
      if n % i == 0:
        return False
    return True

k = int(input('nechta son kiritmoqchisz: '))

count = 0

for i in range(1,k+1):
    n = int(input(f'{i} - sonni kiriting: '))

    if is_prime(n):
        count += 1

print(count)