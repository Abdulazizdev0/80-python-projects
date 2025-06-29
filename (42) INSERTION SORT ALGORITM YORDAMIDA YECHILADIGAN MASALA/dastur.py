

def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        current_value = arr[i]
        position = i - 1

        while position >= 0 and arr[position] > current_value:
            arr[position + 1] = arr[position]
            position -= 1

        arr[position + 1] = current_value

    return arr

print(insertion_sort([10, 2, 9, 3, 1, 8, 7, 3, 4, 5]))
