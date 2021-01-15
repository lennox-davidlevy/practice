# // leetcode 351
# //Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
# //| 1 | 2 | 3 |
# //| 4 | 5 | 6 |
# //| 7 | 8 | 9 |
# //Invalid move: 4 - 1 - 3 - 6
# //Line 1 - 3 passes through key 2 which had not been selected in the pattern.
# //Invalid move: 4 - 1 - 9 - 2
# //Line 1 - 9 passes through key 5 which had not been selected in the pattern.
# //Valid move: 2 - 4 - 1 - 3 - 6
# //Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
# //Valid move: 6 - 5 - 4 - 1 - 9 - 2
# //Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
