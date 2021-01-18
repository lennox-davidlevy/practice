# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.


# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
# Example 4:

# Input: coins = [1], amount = 1
# Output: 1
# Example 5:

# Input: coins = [1], amount = 2
# Output: 2
def coin_change(coins, amount):
    if len(coins) == 0:
        return -1
    dp_array = [amount + 1] * (amount + 1)
    dp_array[0] = 0
    for i in range(0, amount + 1):
        for coin in coins:
            dp_array[i] = min(dp_array[i], 1 + dp_array[i - coin])
    if dp_array[amount] > amount:
        return -1
    else:
        return dp_array[amount]


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1], 0))
print(coin_change([1], 1))
print(coin_change([1], 2))
