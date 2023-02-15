class Solution:
    def maxSubArray(self, nums:list[int]) -> int:
        result = -float("inf")
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:
                result = count
            if count < 0:
                count = 0
        return result


print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4,5,6]))

"""
解题思路
1. 当nums[i] + nums[i+1] < 0 且nums[i+1] > 0时，总和重新计算由nums[i+1] = nums[i]
2. 但凡result还没 < 0 则不会重新开始计算
"""