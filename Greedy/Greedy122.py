class Solution:
    def MaxProfit(self, nums:list[int]) -> int:
        profit = 0
        diff = 0
        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            if diff > 0:
                profit += diff
        return profit
    
    def MaxProfit2(self, nums:list[int]) -> int:
        profit = 0
        for i in range(1, len(nums)):
            profit += max(nums[i] - nums[i-1], 0)
        return profit

"""
解题思路
1. 计算nums[i]和nums[i-1]之间的差值， 当差值为正数为能赚钱则买进反之不买
"""