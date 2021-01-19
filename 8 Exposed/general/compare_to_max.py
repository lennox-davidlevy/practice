# returns largest value in array of n non-negative ints


def compare_to_max(arr, n):
    if n <= 0:
        return -1
    current_max = arr[0]
    for i in range(1, n):
        if arr[i] > current_max:
            current_max = arr[i]
    return current_max


def compare_to_max_square(arr, n):
    if n <= 0:
        return -1
    for i in range(n):
        is_max = True
        for j in range(n):
            if arr[j] > arr[i]:
                is_max = False
                break
        if is_max == True:
            break
    return arr[i]


arr = [1, 5, 3, 13, 5, 234, 5, 1231, 5, 6]
n = len(arr)
print(compare_to_max(arr, n))
print(compare_to_max_square(arr, n))
