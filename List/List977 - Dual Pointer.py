class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        fp, bp, np = 0, n-1, n-1
        ans = [-1] * n
        while fp <= bp:
            fm = nums[fp] ** 2
            bm = nums[bp] ** 2
            if fm > bm:
                ans[np] = fm
                fp += 1
            else:
                ans[np] = bm
                bp -= 1
            np -= 1
        return ans


"""
解题思路
1. 利用双指针思路， 由原数组前后对比大小
2. 大的值就放入新的数组
3. 放入后， 新数组的指针向前移。 而原数组的大值指针向后或向前移。
"""