# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.


# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
# Example 4:

# Input: n = 4
# Output: true
# Example 5:

# Input: n = 5
# Output: false


# def power_of_two(n):
#    for i in range(n):
#        if 2 ** i == n:
#            return True
#    return False
def power_of_two(n):
    while n > 1:
        if n / 2 != n // 2:
            return False
        n = n / 2
    return n == 1


print(power_of_two(1))
print(power_of_two(16))
print(power_of_two(3))
print(power_of_two(4))
print(power_of_two(5))
print(power_of_two(100))
