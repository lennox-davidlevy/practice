# NOT COMPLETE
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


# Example 1:

# Input: arr = [1,2,3,4,5], k = 4, x = 3
# Output: [1,2,3,4]
# Example 2:

# Input: arr = [1,2,3,4,5], k = 4, x = -1
# Output: [1,2,3,4]

# brute force
def k_closest(arr, k, x):
    if len(arr) < k or len(arr) == 0:
        return None
    temp_tuples = []
    for num in arr:
        delta = abs(x - num)
        temp_tuples.append((delta, num))
    sorted_tuples = sorted(temp_tuples, key=lambda temp_tuples: temp_tuples[0])
    result = []
    for i in range(k):
        result.append(sorted_tuples[i][1])
    return sorted(result)


print(k_closest([1, 2, 3, 4, 5], k=4, x=3))
# print(k_closest([1, 2, 3, 4, 5], k=4, x=-1))
print(k_closest([1, 1, 1, 10, 10, 10], 1, 9))


# def k_closest_binary(arr, k, x):
#    start = 0
#    end = len(arr) - k
#    while start < end:
#        mid = (start + end) // 2
#        if x - arr[start] > arr[mid + k] - x:
#            start = mid + 1
#        else:
#            start = mid
#    return arr[start : end + k]
#
#
# print(k_closest_binary([1, 2, 3, 4, 5], k=4, x=3))
## print(k_closest_binary([1, 2, 3, 4, 5], k=4, x=-1))
# print(k_closest_binary([1, 1, 1, 10, 10, 10], 1, 9))
