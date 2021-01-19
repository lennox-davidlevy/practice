# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# def climbing_stairs(n):
#    dp_array = [int for i in range(n + 1)]
#    dp_array[0] = 1
#    dp_array[1] = 1
#    for i in range(2, n + 1):
#        dp_array[i] = dp_array[i - 1] + dp_array[i - 2]
#    return dp_array[n]
#
#
# def climb(n):
#    if n == 1:
#        return 1
#    dp = [int for i in range(n + 1)]
#    dp[0] = 1
#    dp[1] = 1
#    for i in range(2, n + 1):
#        dp[i] = dp[i - 1] + dp[i - 2]
#    return dp[n]
def climbing_stairs(n):
    dp = [int for i in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


print(climbing_stairs(3))
# print(climb(3))
