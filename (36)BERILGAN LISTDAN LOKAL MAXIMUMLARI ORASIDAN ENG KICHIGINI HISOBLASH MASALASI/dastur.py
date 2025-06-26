
def find_small_local_maxima(arr):
    n = len(arr)
    local_maxima = []

    for i in range(1,n-1):
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            local_maxima.append(arr[i])


    if local_maxima:
        return min(local_maxima)
    else:
        return None


print(find_small_local_maxima([1,3,2,4,6,5,9,1]))



