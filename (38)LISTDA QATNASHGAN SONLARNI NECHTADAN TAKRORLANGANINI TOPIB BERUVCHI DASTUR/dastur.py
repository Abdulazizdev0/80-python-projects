


def find_numbers_frequency(arr):
    numbers = []
    frequency = []

    for element in arr:
        if element in numbers:
            index = numbers.index(element)
            frequency[index] += 1
        else:
            numbers.append(element)
            frequency.append(1)

    for i in range(len(numbers)):
        print(f"{numbers[i]} soni  {frequency[i]} ta")

    print(f"numbers: {numbers}")
    print(f"frequency: {frequency}")



find_numbers_frequency([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])