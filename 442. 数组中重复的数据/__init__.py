from typing import List

from Utils.common import run_time

"""
题目：
给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。

找到所有出现两次的元素。

你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？

示例：

输入:
[4,3,2,7,8,2,3,1]

输出:
[2,3]


"""

"""
借用索引号，因为是在1~n之间，那么我们可以用索引0表示数字1，索引1表示数字2...，
当有个数字num，我们将num - 1的位置的数字取相反数，连续两次取相反数会变回来，便可判断元素出现次数。

所以时间复杂度为O(n)

"""


class Solution:

    # 绝对值
    @run_time
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            loc = abs(nums[i]) - 1
            if nums[loc] < 0:
                res.append(loc + 1)
            nums[loc] = -nums[loc]
            print(nums)
        return res


if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    s = Solution()

    print(s.findDuplicates(nums))
