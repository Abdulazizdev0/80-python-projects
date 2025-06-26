

def find_closest(arr,r):
    min_diff = float('inf')
    closest_element = None

    for element in arr:
        diff = abs(element - r)

        if diff < min_diff:
            min_diff = diff
            closest_element = element

    return closest_element

print(find_closest([1,3,2,4,6,5,9,1],5))
