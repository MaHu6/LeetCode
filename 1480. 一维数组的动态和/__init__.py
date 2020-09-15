import time
from typing import List

from Utils.common import run_time

"""
题目：
给你一个数组 nums 。数组「动态和」的计算公式为：runningSum[i] = sum(nums[0]…nums[i]) 。

请返回 nums 的动态和。

 

示例 1：

输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。

"""

"""
注释：
runningSum 
    将累加数放入新数组

runningSum2
    从第 1 个位置开始，累加上一个位置的数字，放入原数组的原位置，不使用额外空间

"""


class Solution:
    @run_time
    def runningSum(self, nums: List[int]) -> List[int]:
        res_nums = []
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            res_nums.append(current_sum)

        return res_nums

    @run_time
    def runningSum2(self, nums: List[int]) -> List[int]:

        for i in range(1, len(nums)):
            nums[i] = nums[i - 1] + nums[i]

        return nums


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(nums)
    s = Solution()

    print(s.runningSum(nums))

    nums = [1, 2, 3, 4]
    print(s.runningSum2(nums))
