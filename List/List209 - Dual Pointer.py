class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        res = float("inf")
        i = 0
        sum = 0
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= target:
                res = min(res, j-i+1)
                sum -= nums[i]
                i += 1
        return 0 if res == float("inf") else res

"""
解题思路
1. 双指针思路
2. 当上指针的值大于target时则动下指针以缩短两个值的距离
"""