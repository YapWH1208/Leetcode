class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        step = 0
        current_distance, next_distance = 0, 0
        for i in range(len(nums)-1):# 不启用数组最后一位数字
            next_distance = max(i+nums[i], next_distance)
            if i == current_distance:
                current_distance = next_distance
                step += 1
        return step

    def jump2(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)
            if i == curDistance: 
                if curDistance != len(nums) - 1:
                    ans += 1
                    curDistance = nextDistance
                    if nextDistance >= len(nums) - 1: break
        return ans


"""
解题思路
1. 计算下一个值得覆盖范围
2. 当前的值得覆盖范围走到头了则利用下一个值得覆盖范围
"""