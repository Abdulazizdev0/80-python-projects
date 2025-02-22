
def digit_count(k):
    count = 0
    while k>0:
        k = k // 10
        count += 1

    return k

number = int(input('sonni kiriting: '))
print(digit_count(number))