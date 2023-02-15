import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0
        odd_num = 0
        for i in collections.Counter(s).values():
            if i >= 2:
                result += i//2 * 2
            if i%2 == 1:
                odd_num = 1
        return result + odd_num

"""
解题思路
1. 利用Counter()对字符串进行收纳规整
2. 找出2以上的字符进行计算
3. 计算奇数字符的存在(这里不计算数量是因为奇数字符只能有一个)
"""