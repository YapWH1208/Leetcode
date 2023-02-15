class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        ans = [[0] * n for _ in range(n)]
        startx, starty = 0, 0
        loop, mid = n//2, n//2
        count = 1

        for offset in range(1, loop+1):
            for i in range(starty, n - offset):
                ans[startx][i] = count
                count += 1
            for i in range(startx, n - offset):
                ans[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):
                ans[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):
                ans[i][starty] = count
                count += 1
            startx += 1
            starty += 1
        
        if n % 2 == 1:
            ans[mid][mid] = count
        return ans

"""
解题思路
1. 利用左闭右开的思路对每一个边进行计算
2. 沿着顺时针的方向进行计算
3. 当n为奇数时，在最后为中心点赋值
"""