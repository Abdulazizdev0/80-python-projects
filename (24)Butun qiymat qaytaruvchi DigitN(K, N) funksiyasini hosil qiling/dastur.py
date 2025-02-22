
def digit_n(k,n):
    str_k = str(k)

    if len(str_k) < n:
        return -1
    else:
        return str_k[n-1]


number = int(input('sonni kiriting: '))
order = int(input('tartib raqamni kiriting: '))

print(number,order)