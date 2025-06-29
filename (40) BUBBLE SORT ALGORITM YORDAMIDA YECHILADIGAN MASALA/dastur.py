

def buble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


print(buble_sort([5,2,3,6,5,6,7,8,9,10]))