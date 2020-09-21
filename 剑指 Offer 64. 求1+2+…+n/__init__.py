from Utils.common import run_time

"""
题目：
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6

"""

"""
sumNums1： 平均计算，需要用到乘除，此题不可用
sumNums2： 迭代 ，需要循环，也不可用
sumNums3： 递归，终止条件为 逻辑判断

"""


class Solution:

    def __init__(self):
        self.res = 0

    @run_time
    def sumNums1(self, n: int) -> int:
        return n * (n + 1) // 2

    @run_time
    def sumNums2(self, n: int) -> int:
        r = 0
        for i in range(n + 1):
            r += i

        return r

    # @run_time
    def sumNums3(self, n: int) -> int:
        n > 1 and self.sumNums3(n - 1)

        self.res += n

        return self.res


if __name__ == '__main__':
    n = 3
    s = Solution()
    print(s.sumNums1(n))
    print(s.sumNums2(n))
    print(s.sumNums3(0))
