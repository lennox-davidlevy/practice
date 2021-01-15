# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Follow up:

# Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
# Could you do it in-place with O(1) extra space?


# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# reverse
# class Solution:
#    def rotate(self, nums, k):
#        n = len(nums)
#        k %= n
#        # reverse entire list
#        self.reverse(nums, 0, n - 1)
#        # reverse first k of list
#        self.reverse(nums, 0, k - 1)
#        # reverse remainder of list
#        self.reverse(nums, k, n - 1)
#        return nums
#
#    def reverse(self, nums: list, start: int, end: int) -> None:
#        while start < end:
#            nums[start], nums[end] = nums[end], nums[start]
#            start, end = start + 1, end - 1


class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        start = count = 0
        while count < n:
            current, prev = start, num[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 100
                if start == current:
                    break
            start += 1


nums = [-1, -100, 3, 99]
k = 2
test = Solution()
print(test.rotate(nums, k))
