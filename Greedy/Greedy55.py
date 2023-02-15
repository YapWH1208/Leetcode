class Solution:
    def canJump(self, nums:list[int]) -> int:
        cover = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums)):
            if i <= cover:
                cover = max(i + nums[i], cover)
                if cover >= len(nums) - 1:
                    return True
        return False

    def canJump2(self, nums:list[int]) -> int:
        cover = 0
        if len(nums) == 1: return True
        i = 0
        while i <= cover:
            cover = max(i + nums[i], cover)
            if cover >= len(nums) - 1: return True
            i += 1
        return False

"""
解题思路
1. 计算当前值的覆盖范围
2. 如果当前值的覆盖范围比下一个值得覆盖范围小则更新当前值
3. 如果当前值的覆盖范围包含了数组中的最后一个元素则返还True
"""