


def EKUB(a,b):
    while b != 0:
        a,b = b,a%b
    return a

def EKUK(a,b):
    ekuk = a * b / EKUB(a,b)

    return ekuk

a = int(input('1 - sonni kiriting: '))
b = int(input('2 - sonni kiriting: '))

print(EKUK(a,b))


