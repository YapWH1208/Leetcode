class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        fast, slow = 0, 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
        return slow


"""
解题思路
1. 利用双指针，快的指针进行探测而慢的指针进行新值的收纳
"""