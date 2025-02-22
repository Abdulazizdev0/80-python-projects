
def is_palindirim(n):
    str_n = str(n)
    return str_n == str_n[::-1]

def count_poly(numbers):
    count = 0
    for number in numbers:
        if is_palindirim(number):
            count += 1

    return count

print(count_poly([12321, 123, 456]))
print(count_poly([101, 121, 131]))
