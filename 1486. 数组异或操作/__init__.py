from Utils.common import run_time

"""
给你两个整数，n 和 start 。

数组 nums 定义为：nums[i] = start + 2*i（下标从 0 开始）且 n == nums.length 。

请返回 nums 中所有元素按位异或（XOR）后得到的结果。


示例 1：

输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。


"""

"""
异或的性质
1) 0 ^ x = x
2) x ^ x = 0
3) 2x ^ (2x+1) = 1

"""


class Solution:
    # 暴力法
    @run_time
    def xorOperation(self, n: int, start: int) -> int:
        res = 0
        for i in range(n):
            res ^= (start + 2 * i)

        return res


if __name__ == '__main__':
    n = 5

    start = 0

    s = Solution()

    print(s.xorOperation(n, start))
