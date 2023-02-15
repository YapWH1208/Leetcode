class Solution:
    def FindContentChildren(self, g:list[int], s:list[int]) -> int:
        g.sort()
        s.sort()

        result = 0

        for i in range(len(s)):
            if result < len(g) and s[i] >= g[result]:
                result += 1
        return result

    def FindContentChildren2(self, g:list[int], s:list[int]) -> int:
        g.sort()
        s.sort()

        start, count = len(s) - 1, 0

        for i in range(len(g) - 1, -1, -1):
            if start >= 0 and g[i] <= s[start]:
                start -= 1
                count += 1
        return count

"""
解题思路
1. 有两种解法：
    - 优先考虑小胃口的孩子
    - 优先考虑大胃口的孩子
2. 小胃口
    把最小的包子分给胃口最小的孩子，如果无法满足胃口则换下一个包子
3. 大胃口
    把大包子给胃口最大的孩子，如果无法满足则给胃口第二大的孩子
"""