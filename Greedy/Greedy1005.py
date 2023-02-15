class Solution:
    def LargestSumAfterKNegations(self, A:list[int], k:int) -> int:
        A = sorted(A, key=abs, reverse=True)
        for i in range(len(A)):
            if k > 0 and A[i] < 0:
                A[i] *= -1
                k -= 1
        if (k % 2) == 1:
            A[-1] *= -1
        #if K > 0:
        #    A[-1] *= (-1)**K
        return sum(A)

"""
解题思路
1. 把数组按照绝对值大小逆序进行排序
2. 把数组中的负数进行置换（*-1）
    - 优先考虑数组中靠前的负数
3. 如果k值还没用完则应对不一样的情况进行处理
    - 若k值%2 == 1, 则对数组中最后一位进行置换
    - 若k值%2 == 0，则无视
** 另外一种剩余k值得处理方案为吧数组中最后一个元素与-1的k次方进行相乘
"""