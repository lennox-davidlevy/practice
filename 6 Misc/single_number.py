# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1


def single_number(arr):
    if len(arr) == 1:
        return arr[0]
    num_hash = {}
    for num in arr:
        num_hash[num] = num_hash.get(num, 0) + 1
    for num, val in num_hash.items():
        if val == 1:
            return num
    return None


print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))
