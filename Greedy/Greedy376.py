class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        preC, curC, result = 0,0,1  #题目里nums长度大于等于1，当长度为1时，其实到不了for循环里去，所以不用考虑nums长度
        for i in range(len(nums) - 1):
            curC = nums[i + 1] - nums[i]
            if curC * preC <= 0 and curC !=0:  #差值为0时，不算摆动
                result += 1
                preC = curC  #如果当前差值和上一个差值为一正一负时，才需要用当前差值替代上一个差值
        return result

"""
解题思路
1. 要考虑三种情况：
    - 上下坡有平坡
    - 上上坡/下下坡（单调坡）有平坡
    - 数组的两个尾端
2. 比较一个节点与前后节点的前后差异，若为相乘结果为负数则为拐点（正数与负数相乘为负数）
"""