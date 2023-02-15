class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        start = 0
        curSum = 0
        totalSum = 0
        for i in range(len(gas)):
            curSum += gas[i] - cost[i]
            totalSum += gas[i] - cost[i]
            if curSum < 0:
                curSum = 0
                start = i + 1
        if totalSum < 0: return -1
        return start

    def canCompleteCircuit2(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        cur_sum = 0
        min_sum = float('inf')
        
        for i in range(n):
            cur_sum += gas[i] - cost[i]
            min_sum = min(min_sum, cur_sum)
        
        if cur_sum < 0: return -1
        if min_sum >= 0: return 0
        
        for j in range(n - 1, 0, -1):
            min_sum += gas[j] - cost[j]
            if min_sum >= 0:
                return j
        
        return -1

"""
解题思路
1. 利用gas和cost的差值寻找当前和
2. 当当前和小于0时则有i+1作为新的起点重新计算
2. 当总和<0则return-1
"""