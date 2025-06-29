
def find_ser(arr):
    b = []
    c = []

    n = len(arr)
    current_value = arr[0]
    count = 1

    for i in range(1, n + 1):
        if i < n and arr[i] == current_value:
            count += 1
        else:
            c.append(current_value)
            b.append(count)

            if i < n:
                current_value = arr[i]
                count = 1

    return b,c

resultb1,resultc1 = find_ser([1,1,1,2,2,3,4,5,5,5])

print(f"b:{resultb1},c:{resultc1}")
print(resultc1)


