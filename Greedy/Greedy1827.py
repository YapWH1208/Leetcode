class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                diff = nums[i] - nums[i+1]
                nums[i+1] += diff + 1
                ans += diff + 1
        return ans

"""
解题思路
1. 计算nums[i]和nums[i+1]的差值
2. 对nums[i+1]进行差值补位
"""